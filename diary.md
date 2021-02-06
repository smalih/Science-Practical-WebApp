### Diary

This diary will help me keep track of progress made, and what needs to be done. At the end of this diary, there is an up-to-date list of tasks that need to be achieved.

10/01/2021 - Added frontend and backend support for username, and created a table in html for practical data. Idea is to process practical data as a pandas df and but convert it into sql before storing it in the practical data db (need to add a results df column).
             Next step si to figure out how to POST data from the html table to the backend, convert it into a pandas df (to use for plotting with numpy) and then convert it into sql.
        
30/01/2021 - Html table that was created last session has now been integrated to make use of flask-forms and the Jinja-template. More database relationships have been added as the requirements continue to evolve. It has come to light that when calculating the mean, we do not want to account for anomalous data so the user will be given an option to mark anomalous data. Although, in the future, research into anomaly detection algorithms may be explored. There is now a seperate table for the trial entries, with the following columns: anomalous dv_value value trial_no practical_data(FOREIGN_KEY)

Another problem that has arisen is that although I may be able to take in the trial data, how can I ensure that each entry for the IV is stored with reference to its corresponding DV. It is considered bad practice to store key_value pairs in database tables (hence the dv_value column). First normal form (1NF) states that 'the domain of each attribute must be atomic (indivisible) , and the value of each attribute must be a single value from the domain.'

Upon reflection, I am content with the progress made. Today, I have learned a little more about good practices regarding databases, and how to POST multiple forms to a single form handler. You may have noticed that an extensible period of time has passed since the last session. There were many factors contributing towards this; however, I have realised that the longer I do not attend to this project, the more my enthusiasm and excitement for the project shrinks. Fortunately, this session was apt for relighting my fuel. I must be careful in the future to not be caught by this trap again and fall into an even deeper slumber.

05/02/2021 - Today, I stumbled, or restumbled should I say, upon a very useful python framework. 
Dash - 'Dash is a productive Python framework for building web analytic applications. Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.'

The Dash framework seems perfect for this project. The framework can provide editable datatables, where users can even choose to add or remove rows and columns. I am certainly excited about coming to grips with this framework, as it can help speed up the development process. The downside is that this is a new framework I ahve to learn, although the tutorials seem fairly comprehensive.

06/02/2021 - I have decided to move this diary into the main branch, as there is no need to have a diary in seperate branches, plus redecues the potential for confusion and inconsistencies when it comes to updating the diary several times in various branches, it is much better to to keep it central.

Much progress has been made, mainly that I have familiarised myself a little more with Dashly. As I see it, I have two options open to me. I can choose to host most of the web app as a Dash application (rather than Flask), because the web app is mainly about the analysis of practical data. Contrastingly, I can choose to host only the necessary parts of the application as a Dash app. The problem is that this may make things a lot more complicated, especially when it omes to routing between Dash and Flask apps as Dash does not support URL routes - a multipage application in Dash requires mutliple Dash applications to be iniated, which may cause performance issues.

Another problem is styling the Dash html. I know how to apply a stylesheet within a Flask application, and the documentation shows to apply a stylesheet to a Dash app, but applying a stylesheet to a Dash applicationw embedded insdie a Flask application seems to be a little more tricky. I suspect that it will be sussed out by the end of the next session. I am certainly excited about moving past the state of 'rewriting code' and getting to actually write fresh code using the Dash framework.

### Tasks:
<ul>
  <Apply css stylesheet(s) to Dash html</li>
  <li>Create a practical data table that will store practical data read in from pandas df</li>
  <li>Practical (Routes)</li>
  <ol>
    <li>Logic for parsing data sent from the client-side (html table mainl)</li>
    <li>POST data from the html table to the backend</li>
   </ol>
  <li>Convert data into a pandas df (to use for plotting with numpy)</li>
  <li>Connvert data into SQL for storage in practical data db</li>
  <li>Design and code logic for plot_practical method - Are there better alternatives for more sophisticated data visualisation?</li>
  <li>Unit Testing</li>
</ul>
