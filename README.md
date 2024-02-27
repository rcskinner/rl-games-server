# rl-games-server
A repository for hosting a games server, part of a personal project to get a deeper understanding of the following: 
- Reinforcement Learning 
- Deploying applications / systems of applications on k8s 
- Monitoring the above with Datadog

# Related repositories: 
- rl-games-agent: Code for an agent to play the games
- rl-games-hosting: k8s infrastructure for hosting and monitoring the system

# Minimum Viable Product 
- **Iteration 1: Game server that hosts connect4 game**
    - Randomly plays Red/Black until a tie or a wins is achieved
    - Gamestate stored locally
- **Iteration 2: Game server that hosts a connect4 game**
    - Exposes an API allowing one player to play against a random choice generated locally
    - Gamestate stored externally in a cache/database
- **Iteration 3: Gameserver able to host multiple games at once**
    - One random game occuring 
    - One human player against random