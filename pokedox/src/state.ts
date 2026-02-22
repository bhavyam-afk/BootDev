import { createInterface, type Interface } from "readline";
import { getCommands } from "./commands.js";
import { PokeAPI, Pokemon } from "./pokeapi.js";

export type CLICommand = {
  name: string;
  description: string;
  callback: (state: State, ...args: string[]) => Promise<void>;
};

export type State = {
    commands: Record<string, CLICommand>;
    rl: Interface;
    pokeapi: PokeAPI;
    nextLocationsURL: string | null;
    prevLocationsURL: string | null;
    pokedex: Record<string, Pokemon>;
}

export function initState(): State{
    const rl = createInterface({
            input: process.stdin,
            output: process.stdout,
            prompt: "pokedex> ",
        });
    
    const commands = getCommands();

    const pokeapi = new PokeAPI()
    
    return {
        rl,
        commands,
        pokeapi,
        nextLocationsURL: null,
        prevLocationsURL: null,
        pokedex: {},
    };
}

