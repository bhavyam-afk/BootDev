import { State } from "./state.js";

export function cleanInput(input: string): string[] {
    let cleaned = input.toLowerCase().split(" ")
    cleaned = cleaned.map((word) => word.trim())
    return cleaned.filter((word)=> word.length > 0)
}

export function startREPL(state: State): void {
    state.rl.prompt();

    state.rl.on("line", async (input: string) => {
        const words = cleanInput(input);
        
        if (words.length === 0) {
            state.rl.prompt();
            return;
        }
        else if(words[0] in state.commands){
            try {
                const [command, ...args] = words;
                await state.commands[command].callback(state, ...args);
            } catch (error) {
                console.error(`Error executing command: ${error}`);
            }
        }
        else{
            console.log(`Your command was: ${words[0]}`);
        }
        state.rl.prompt();
    });
}