# TODO
[Note: This is more of a document designed to give the reader an idea of where the project is headed. For a more in-depth, bulleted, detailed todo list, watch this repository.]

## Contents

[Base Features](#base-features)<br>
[Feature Releases](#feature-releases)


## Base Features
Core features of web application that need to be completed


### Server-side processing of practical data
Add all practical data to database. Needs to be processed into columns of the following:
<ul>
  <li>Title</li>
  <li>Degree of Study</li>
  <li>Subject</li>
  <li>Equipment</li>
  <li>Method</li>
  <li>Results Table</li>
  <li>Graph (default=line graph)</li>
  <li>Hazards</li>
  <li>Additional Notes</li>
</ul>

This will require lots of manual work and man-hours. Will consist of:
<ol>
  <li>Manually copying various practical information into a text-file with a consistent format</li>
    --> Formatting and tidying up data for each practical
  <li>Having default values for each field for each practical</li>
</ol>

Note: One thing that needs to be considered is how the practical data will be 'translated' to the client-side. What needs to be achieved is that users that are not logged in (or have not changed any practical data) will be displayed default practical data. If they are logged in, they will first have the additional option of customising the practical data. This customisation then needs to be saved and override default data for that specific user.

Considering data visualisation, it should be considered that some practical data is better displayed as a bar or pie chart rather than line graph, depending on the practical. In addition, some data may require more than one type of data visualisation to be displayed at once.

### Data Visualisation
Data needs to be displayed within the webpage. Default dispay of data should be appropriate graph with labeled axes and corresponding results table

## Feature Releases
Going into the future, looking at the prospect of making this product an online service. Moreover, also looking at in the future, approaching schools with this product.
