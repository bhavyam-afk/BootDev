import { State, CLICommand } from "./state.js";

export async function CommandExit(state: State): Promise<void>{
    console.log("Closing the Pokedex... Goodbye!");
    state.rl.close();
    process.exit(0);
}

export async function CommandHelp(state: State): Promise<void>{
    console.log("Welcome to the Pokedex!")
    console.log("Usage:\n\n")
    for(const c in state.commands){
        console.log(`- ${state.commands[c].name}: ${state.commands[c].description}`)
    }
}

export async function CommandMap(state: State): Promise<void>{
    const locations = await state.pokeapi.fetchLocations(state.nextLocationsURL || undefined);
    state.nextLocationsURL = locations.next;
    state.prevLocationsURL = locations.previous;
    
    for (const location of locations.results) {
        console.log(location.name);
    }
}

export async function CommandMapb(state: State): Promise<void>{
    if (!state.prevLocationsURL) {
        console.log("You're on the first page!");
        return;
    }
    
    const locations = await state.pokeapi.fetchLocations(state.prevLocationsURL);
    state.nextLocationsURL = locations.next;
    state.prevLocationsURL = locations.previous;
    
    for (const location of locations.results) {
        console.log(location.name);
    }
}

export async function CommandExplore(state: State, ...args: string[]): Promise<void>{
    if (args.length === 0) {
        console.log("Please provide a location area name.");
        return;
    }
    
    const areaName = args[0];
    const location = await state.pokeapi.fetchLocation(areaName);
    
    console.log(`Exploring ${location.name}...`);
    console.log("Found Pokemon:");
    for (const encounter of location.pokemon_encounters) {
        console.log(`  - ${encounter.pokemon.name}`);
    }
}

export async function CommandInspect(state: State, ...args: string[]): Promise<void>{
    if (args.length === 0) {
        console.log("Please provide a Pokemon name.");
        return;
    }
    
    const pokemonName = args[0].toLowerCase();
    const pokemon = state.pokedex[pokemonName];
    
    if (!pokemon) {
        console.log("you have not caught that pokemon");
        return;
    }
    
    console.log(`Name: ${pokemon.name}`);
    console.log(`Height: ${pokemon.height}`);
    console.log(`Weight: ${pokemon.weight}`);
    console.log("Stats:");
    for (const stat of pokemon.stats) {
        console.log(`  -${stat.stat.name}: ${stat.base_stat}`);
    }
    console.log("Types:");
    for (const typeInfo of pokemon.types) {
        console.log(`  - ${typeInfo.type.name}`);
    }
}

export async function CommandCatch(state: State, ...args: string[]): Promise<void>{
    if (args.length === 0) {
        console.log("Please provide a Pokemon name.");
        return;
    }
    
    const pokemonName = args[0];
    console.log(`Throwing a Pokeball at ${pokemonName}...`);
    
    const pokemon = await state.pokeapi.fetchPokemon(pokemonName);
    
    // Calculate catch chance based on base_experience
    // Higher base_experience = harder to catch
    const maxChance = 255;
    const catchChance = maxChance - (pokemon.base_experience / 100);
    const random = Math.random() * maxChance;
    
    if (random < catchChance) {
        console.log(`${pokemonName} was caught!`);
        state.pokedex[pokemon.name] = pokemon;
    } else {
        console.log(`${pokemonName} escaped!`);
    }
}

export function getCommands(): Record<string, CLICommand> {
  return {
    exit: {
      name: "exit",
      description: "Exits the pokedex",
      callback: CommandExit,
    },
    help: {
        name: "help",
        description: "Displays a help message",
        callback: CommandHelp,
    },
    map: {
        name:"map",
        description: "Displays next 20 locations.",
        callback: CommandMap,
    },
    mapb: {
        name: "mapb",
        description: "Displays previous 20 locations.",
        callback: CommandMapb,
    },
    explore: {
        name: "explore",
        description: "Displays a specific location's pokemons",
        callback: CommandExplore,
    },
    catch: {
        name: "catch",
        description: "Attempt to catch a pokemon by name",
        callback: CommandCatch,
    },
    inspect: {
        name: "inspect",
        description: "Inspect a caught pokemon by name",
        callback: CommandInspect,
    }
  };
}