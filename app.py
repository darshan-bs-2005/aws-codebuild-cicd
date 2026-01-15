from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Snakes and Ladders positions
snakes = {
    16: 6,
    48: 26,
    49: 11,
    56: 53,
    62: 19,
    64: 60,
    87: 24,
    93: 73,
    95: 75,
    98: 78
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100
}

player_position = 0

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Snake & Ladder</title>
</head>
<body>
    <h1>Snake & Ladder Game</h1>
    <h2>Player Position: {{ pos }}</h2>

    <form method="POST">
        <button type="submit">Roll Dice 🎲</button>
    </form>

    {% if dice %}
        <p>You rolled: <strong>{{ dice }}</strong></p>
    {% endif %}

    {% if msg %}
        <p>{{ msg }}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def game():
    global player_position
    dice = None
    msg = ""

    if request.method == "POST":
        dice = random.randint(1, 6)
        player_position += dice

        if player_position > 100:
            player_position -= dice
            msg = "Need exact roll to reach 100!"
        else:
            if player_position in snakes:
                msg = f"Oh no! Snake bit you! Go down to {snakes[player_position]}."
                player_position = snakes[player_position]

            elif player_position in ladders:
                msg = f"Yay! Ladder up to {ladders[player_position]}."
                player_position = ladders[player_position]

            if player_position == 100:
                msg = " You won the game! Restarting..."
                player_position = 0

    return render_template_string(
        html_page,
        pos=player_position,
        dice=dice,
        msg=msg
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
