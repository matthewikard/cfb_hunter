import streamlit as st
from game_engine import Game
from data import teams, categories

st.title("CFB Hunter")

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if st.session_state.feedback:
    st.info(st.session_state.feedback)
    st.session_state.feedback = None

# --- Initialize game state ---
if "game" not in st.session_state:
    st.session_state.game = Game(teams, categories)

game = st.session_state.game

# --- Game loop (UI-driven) ---
if not game.is_complete():
    team = game.current_team()

    st.subheader(f"Team: {team['school']}")

    available = game.available_categories()

    st.metric(
    label="Total Score",
    value=game.score()
    )   

    st.header("Categories")

    for category in game.categories:
        col_cat, col_team = st.columns([2, 3])

        with col_cat:
            st.write(category)

        with col_team:
            if category in game.assignments:
                assigned_team = game.assignments[category]
                st.write(
                    f"{assigned_team['school']} "
                    f"({assigned_team['metrics'][category]})"
                )
            else:
                st.write("—")


    choice = st.radio(
        "Available Categories",
        available,
        key=f"choice_{game.current_index}"
    )

    if st.button("Submit"):
        # Compute best possible category for current team
        best_category = min(
            available,
            key=lambda c: team["metrics"][c]
        )

        chosen_value = team["metrics"][choice]
        best_value = team["metrics"][best_category]

        if choice == best_category:
            feedback = (
                f"Optimal choice! {choice} was the best possible category "
                f"({chosen_value})."
            )
        else:
            feedback = (
                f"Better option available: {best_category} "
                f"({best_value}). You chose {choice} ({chosen_value})."
            )

        st.session_state.feedback = feedback

        game.assign(choice)
        st.rerun()


else:
    st.success("Game Complete!")
    st.write("Final Score:", game.score())

    st.write("Assignments:")
    for cat, team in game.assignments.items():
        st.write(
            f"{cat}: {team['school']} "
            f"({team['metrics'][cat]})"
        )

if st.button("Restart"):
    del st.session_state.game
    st.rerun()
