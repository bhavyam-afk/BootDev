import { Cache } from "./pokecache.js";

export class PokeAPI {
  private static readonly baseURL = "https://pokeapi.co/api/v2";
  private cache: Cache;

  constructor() {
    this.cache = new Cache(5 * 60 * 1000); // 5 minutes
  }

  async fetchLocations(pageURL?: string): Promise<ShallowLocations> {
    const url = pageURL || `${PokeAPI.baseURL}/location-area`;
    
    // Check cache first
    const cached = this.cache.get<ShallowLocations>(url);
    if (cached) {
      return cached;
    }
    
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch locations: ${response.statusText}`);
    }
    const data = await response.json();
    
    // Add to cache
    this.cache.add(url, data);
    
    return data;
  }

  async fetchPokemon(pokemonName: string): Promise<Pokemon> {
    const url = `${PokeAPI.baseURL}/pokemon/${pokemonName.toLowerCase()}`;
    
    // Check cache first
    const cached = this.cache.get<Pokemon>(url);
    if (cached) {
      return cached;
    }
    
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch pokemon: ${response.statusText}`);
    }
    const data = await response.json();
    
    // Add to cache
    this.cache.add(url, data);
    
    return data;
  }

  async fetchLocation(locationName: string): Promise<Location> {
    const url = `${PokeAPI.baseURL}/location-area/${locationName}`;
    
    // Check cache first
    const cached = this.cache.get<Location>(url);
    if (cached) {
      return cached;
    }
    
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Failed to fetch location: ${response.statusText}`);
    }
    const data = await response.json();
    
    // Add to cache
    this.cache.add(url, data);
    
    return data;
  }
}

export type ShallowLocations = {
  count: number;
  next: string | null;
  previous: string | null;
  results: Array<{
    name: string;
    url: string;
  }>;
};

export type Location = {
  id: number;
  name: string;
  region: {
    name: string;
    url: string;
  };
  names: Array<{
    name: string;
    language: {
      name: string;
      url: string;
    };
  }>;
  game_indices: Array<{
    generation: {
      name: string;
      url: string;
    };
    game_index: number;
  }>;
  areas: Array<{
    name: string;
    url: string;
  }>;
  pokemon_encounters: Array<{
    pokemon: {
      name: string;
      url: string;
    };
    version_details: Array<{
      version: {
        name: string;
        url: string;
      };
      max_chance: number;
    }>;
  }>;
};

export type Pokemon = {
  id: number;
  name: string;
  base_experience: number;
  height: number;
  weight: number;
  stats: Array<{
    stat: {
      name: string;
      url: string;
    };
    base_stat: number;
    effort: number;
  }>;
  types: Array<{
    slot: number;
    type: {
      name: string;
      url: string;
    };
  }>;
  abilities: Array<{
    ability: {
      name: string;
      url: string;
    };
    is_hidden: boolean;
    slot: number;
  }>;
};