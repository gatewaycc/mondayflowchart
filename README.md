## Facilities Project Intake Form
* Form URL: [https://forms.monday.com/forms/94b24a47ade146e00f794d2a620febf2](https://forms.monday.com/forms/94b24a47ade146e00f794d2a620febf2)
* Board URL: [https://gateway-cc.monday.com/boards/475894573](https://gateway-cc.monday.com/boards/475894573)

The facilities project intake form will have a dropdown where the requester will choose an AVP/Dean.  The selected AVP/Dean will be sent an email where they approve or deny the proposed project.  If approved, an email is sent to the Project Manager requesting quotes for the project from the involved departments.  After the quotes are inputted, an email is sent to the corresponding VP based on the AVP/Dean selection.  If approved, a confirmation email is sent to the Project Manger.  



## What are we building?
We're building the automations and integrations necessary for the Facilities Project Intake Form.  There are two parts to this:
1. We will be building out a GUI for a flowchart sequence possibly using a Switch Statement in Python.
2. We will be creating in-email button triggers so when the AVP/Dean/VP clicks on Approve or Deny, the status is changed in monday.com.


### Tasks for Part 1
- [x] Determine process flowchart
- [x] Connect Python with Monday
- [ ] switch statement emails selected AVP/Dean
- [ ] when statement for approval that triggers email to PM
- [ ] when statement for quote is entered, trigger email to VP
- [ ] when statement for approval that triggers email to PM


### Possible Monday Automation Format
When _AVP status_ is selected, send _email_.

When _number_ is _greater than_ a _value_ and _AVP dropdown_ is selected, send _email_ to _VP dropdown_.

---


##  Support Documentation:
* Python Quickstart Guide: [https://support.monday.com/hc/en-us/articles/360013483119](https://support.monday.com/hc/en-us/articles/360013483119)
* Overview: [https://monday.com/developers/apps/manage](https://monday.com/developers/apps/manage)
* Monday Playground: [https://gateway-cc.monday.com/apps/playground](https://gateway-cc.monday.com/apps/playground)
* Community Forums: [https://community.monday.com/](https://community.monday.com/)
* Pip Install Monday: [https://pypi.org/project/monday/](https://pypi.org/project/monday/)
* Monday API: [https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API-](https://support.monday.com/hc/en-us/articles/360005144659-Does-monday-com-have-an-API-)
* GraphQL: [https://graphql.org/learn/queries/](https://graphql.org/learn/queries/)

### Notes
* If modules are disconnected, open Administrator CMD and navigate to python scripts path _cd (C:\Program Files (x86)\Python38-32\Scripts)_ and then run the module installation _pip.exe install (monday)_