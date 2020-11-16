# TODO LIST

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
  <li>Hazards</li>
  <li>Additional Notes</li>
</ul>

This will require lots of manual work and man-hours. Will consist of:
<ol>
  <li>Manually copying various practical information into a text-file with a consistent format</li>
    --> Formatting and tidying up data for each practical
  <li>Reading in text-files and processing them as Database Models</li>
  <li>Having default values for each field for each practical</li>
</ol>

Note: One thing that needs to be considered is how the practical data will be 'translated' to the client-side. What needs to be achieved is that users that are not logged in (or have not changed any practical data) will be displayed default practical data. If they are logged in, they will first have the additional option of customising the practical data. This customisation then needs to be saved and override default data for that specific user.

## Feature Releases
