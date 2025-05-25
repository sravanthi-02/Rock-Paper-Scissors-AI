import random

# Memory for opponent history and prediction stats
opponent_history = []
guess_history = {"R": 0, "P": 0, "S": 0}

def player(prev_play):
    global opponent_history, guess_history

    if prev_play:
        opponent_history.append(prev_play)

    # Use a default move for the first few rounds
    if len(opponent_history) < 5:
        return "R"

    # Build a pattern model based on last 3 opponent moves
    pattern = "".join(opponent_history[-3:])
    predictions = {"R": 0, "P": 0, "S": 0}

    for i in range(len(opponent_history) - 3):
        key = "".join(opponent_history[i:i+3])
        if key == pattern:
            next_move = opponent_history[i+3]
            predictions[next_move] += 1

    # Predict the opponent's next move
    if sum(predictions.values()) == 0:
        guess = random.choice(["R", "P", "S"])
    else:
        guess = max(predictions, key=predictions.get)

    # Counter the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[guess]
