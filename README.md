# system_view

<h4>Problem Statement:</h4>
<p>
In R4+ release of ameyo, Supervisor does not have an option to look through the agent activity at system level, and thus have to go through campaign by campaign to get the basic info about agent status. This is not feasible to do so, when we have large number of campaigns.
</p>
<h4>Proposed solution:</h4> 
<p>
Written an appliction in Python using Pyqt5 as the UI library and psycopg2 for database connections.<br>
All the information are computed from the database actions and are presented on the UI.<br>
The Information Presented on UI Includes:
</p> 
<ul>
  <li>Available: Count and % of total logged in user</li>
  <li>Autocall: Count and % of total user with Autocall ON</li>
  <li>List of all users which are logged in and have status set to ready</li>
  <li>List of all users which are unavailable or logged out</li>
  <li>List of all available users is color coded to show which agent has Autocall ON and which has Autocall OFF</li>
 </ul>
<iframe style="width:100%;height:auto;display:block;margin-left:auto;margin-right:auto;" src="https://www.youtube.com/embed/FPY1_pfbBiI">
</iframe>
