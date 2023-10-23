# CIEM6302
Project for Kotug

Understanding project organization and methodologies:

Welcome to the project's readme file. This document is your guide to understanding the organization of our project files and the methodologies employed for data processing and predictions. It's highly recommended to read the outline of each file to grasp its structure and navigate between sections seamlessly. Moreover, the markdowns embedded within each file (as well as the comments in the code) offer valuable insights into the storyline, the code, and the overall methodology employed throughout the project. 

The project is structured into two primary files: "Data_preparation" and "Predictions." Within the "Data_preparation" file, you will find the necessary data processing steps, while the "Predictions" file contains the methods and algorithms utilized for predicting pick-up and drop-off locations. Throughout both files, visualizations are strategically placed to enhance comprehension. Some steps of the data processing and prediction stages are visually represented, aiding readers in grasping the methodologies employed during the project.


Two distinct approaches are implemented to tackle the problem at hand: the "Area approach" and the "Trajectory approach." Both methods are delineated within each file. However, both approaches share a common starting point within the "Data_preparation" file. Here, fundamental data processing tasks applicable to both methods are addressed. Careful attention to this shared section ensures a strong foundation for the subsequent steps unique to each approach.

The "Area approach" involves partitioning the entire water expanse within the Port of Rotterdam into smaller squares encapsulated within polygons. Adjusting the size of these squares is pivotal, with the parameter "diagonal_length_meters" requiring meticulous evaluation. Finding the optimal balance between computational feasibility and accuracy is paramount. While increasing the number of smaller squares refines the discretization, it's imperative to acknowledge computational limitations. Striking a balance that aligns available computational resources with precision is vital for a seamless integration into the predictive model. 

Conversely, the "Trajectory approach" focuses on identifying the top 10 most frequently used havens. For each of these havens, trajectories representing vessel paths to and from the haven are derived. This process involves clustering all pick-up and drop-off locations associated with a specific harbor. The shortest path algorithm is then applied to generate the trajectory, effectively mapping the routes taken by vessels arriving at or departing from the haven.


In addition to the information provided in this file, essential aspects of the project, including the rationale behind utilizing both the "Area approach" and the "Trajectory approach" along with the outcomes and concluding remarks, are documented within the "Predictions" file. Here, readers can find a comprehensive overview of the project's results, the comparative analysis of the two methods, and the final conclusions drawn from the research.

For a deeper understanding of the variables chosen and other intricate project details, readers can explore the "Data_preparation" file. This file contains explanations regarding the selection of specific variables and provides additional contextual information about various aspects of the project's data processing and preparation stages.

