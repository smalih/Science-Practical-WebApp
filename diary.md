### Diary

This diary will help me keep track of progress made, and what needs to be done. At the end of this diary, there is an up-to-date list of tasks that need to be achieved.

10/01/2021 - Added frontend and backend support for username, and created a table in html for practical data. Idea is to process practical data as a pandas df and but convert it into sql before storing it in the practical data db (need to add a results df column).
             Next step si to figure out how to POST data from the html table to the backend, convert it into a pandas df (to use for plotting with numpy) and then convert it into sql.
        
30/01/2021 - Html table that was created last session has now been integrated to make use of flask-forms and the Jinja-template. More database relationships have been added as the requirements continue to evolve. It has come to light that when calculating the mean, we do not want to account for anomalous data so the user will be given an option to mark anomalous data. Although, in the future, research into anomaly detection algorithms may be explored. There is now a seperate table for the trial entries, with the following columns: anomalous dv_value value trial_no practical_data(FOREIGN_KEY)

Another problem that has arisen is that although I may be able to take in the trial data, how can I ensure that each entry for the IV is stored with reference to its corresponding DV. It is considered bad practice to store key_value pairs in database tables (hence the dv_value column). First normal form (1NF) states that 'the domain of each attribute must be atomic (indivisible) , and the value of each attribute must be a single value from the domain.'

Upon reflection, I am content with the progress made. Today I learnt a little more about good practices regarding databases, and how to POST multiple forms to a single form handler. You may have noticed that an extensible period of time has passed since the last session. There were many factors contributing towards; however, I have realised that the longer I did not attend to this project, the more my enthusiasm and exictement about the project shrank. Fortunately, this session was apt for relighting my fuel. I must be careful in the future to not be caught by this trap and fall into a deep slumber.

### Tasks:
<ul>
  <s><li>Create a practical data table that will store practical data read in from pandas df</li></s>
  <li>Practical (Routes) - Logic for parsing data sent from the client-side (html table mainl)<li>
  <li>POST data from the html table to the backend</li>
  <li>Convert data into a pandas df (to use for plotting with numpy)</li>
  <li>Connvert data into SQL for storage in practical data db</li>
  <li>Design and code logic for plot_practical method - Are there better alternatives for more sophisticated data visualisation?</li>
  <li>Unit Testing</li>
</ul>
