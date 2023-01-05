import pandas
import turtle

# Initialize screen with map
screen = turtle.Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import data from CSV
imported_data = pandas.read_csv("50_states.csv")

# Initialize variables
states_guessed = []
correct_answers = 0

# Play game
while len(states_guessed) < 50:
    # Get a state name from the player
    answer = screen.textinput(title=f"{correct_answers}/50 States Correct",
                                    prompt="What is a state's name?").title()

    # If answer has already been guessed, ask again
    if answer in states_guessed:
        continue

    # If answer is a state, label the state on the map image
    if answer in set(imported_data.state):
        # Collect state's info
        state_data = imported_data[imported_data.state == answer]

        # Create new label object
        label = turtle.Turtle()
        label.hideturtle()
        label.penup()

        # Move position to coordinates in state's data
        label.setposition(int(state_data.x), int(state_data.y))

        # Write state's name on label
        label.write(state_data.state.item())

        # Add state to states_guessed
        states_guessed.append(answer)

        # Increase correct_answers by one
        correct_answers += 1
