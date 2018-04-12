import visuals as vs
#environment.py changes:
#'enforce_deadline' -is set to True to force the driving agent to capture whether it reaches the destination in time.
#'update_delay' - is set to a small value (such as 0.01) to reduce the time between steps in each trial.
#'log_metrics' - is set to True to log the simluation results as a .csv file in /logs/.
#'n_test' - is set this to '10' to perform 10 testing trials.

vs.plot_trials('sim_no-learning.csv')

#random actions, hence only a 20% success rate above.

#Now identifying states for better states an agent can be in:
#Inspecting the 'build_state()' agent function shows that the driving agent is given the following data from the environment:
##'waypoint', which is the direction the Smartcab should drive leading to the destination, relative to the Smartcab's heading.
##'inputs', which is the sensor data from the Smartcab. It includes:
###'light', the color of the light.
###'left', the intended direction of travel for a vehicle to the Smartcab's left. Returns None if no vehicle is present.
###'right', the intended direction of travel for a vehicle to the Smartcab's right. Returns None if no vehicle is present.
###'oncoming', the intended direction of travel for a vehicle across the intersection from the Smartcab. Returns None if no vehicle is present.
##'deadline', which is the number of actions remaining for the Smartcab to reach the destination before running out of time.

#The following state space results:
#('is_raining', 'is_foggy', 'is_red_light', 'turn_left', 'no_traffic', 'previous_turn_left', 'time_of_day')

#To implement Q-Learning:
#make following changes in environment.py:
#'enforce_deadline' - is set to True to force the driving agent to capture whether it reaches the destination in time.
#'update_delay' - is set to a small value (such as 0.01) to reduce the time between steps in each trial.
#'log_metrics' - is set to True to log the simluation results as a .csv file and the Q-table as a .txt file in /logs/.
#'n_test' - is set to '10' to perform 10 testing trials.
#'learning' - is set to 'True' to tell the driving agent to use the Q-Learning implementation.

vs.plot_trials('sim_default-learning.csv')

#Almost 60% success rate achieved, but still not good enough.
#Tuning parameters is required.
#In theory, we could allow the agent to learn for an incredibly long amount of time;
#however, another goal of Q-Learning is to transition from experimenting with unlearned behavior to acting on learned behavior.

#Improved Q-Learning Results:
#make following changes to environment.py:
#'enforce_deadline' - Set this to True to force the driving agent to capture whether it reaches the destination in time.
#'update_delay' - Set this to a small value (such as 0.01) to reduce the time between steps in each trial.
#'log_metrics' - Set this to True to log the simluation results as a .csv file and the Q-table as a .txt file in /logs/.
#'learning' - Set this to 'True' to tell the driving agent to use your Q-Learning implementation.
#'optimized' - Set this to 'True' to tell the driving agent you are performing an optimized version of the Q-Learning implementation.
#'n_test' - Set this to some positive number (previously 10) to perform that many testing trials.
#'alpha' - Set this to a real number between 0 - 1 to adjust the learning rate of the Q-Learning algorithm.
#'epsilon' - Set this to a real number between 0 - 1 to adjust the starting exploration factor of the Q-Learning algorithm.
#'tolerance' - set this to some small value larger than 0 (default was 0.05) to set the epsilon threshold for testing.
vs.plot_trials('sim_improved-learning.csv')
