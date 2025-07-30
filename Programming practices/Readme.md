Describe and explain how you used a range of good programming practices in your project. Label each practice used and include a screenshot or code snippet that clearly shows its use related to your description and explanation.

- clear and uncluttered mainline
<img width="469" height="181" alt="image" src="https://github.com/user-attachments/assets/0b0306ae-03e2-4a38-a6bc-85a3d393f9a3" />

A mainline that is logical and simple as it comes: the if condition checks if the script is run directly, when true it initalizes car model database and calls main() which calls run_demo() where the logic for input statements is held.



- one logical task per subroutine
<img width="804" height="274" alt="image" src="https://github.com/user-attachments/assets/9b269227-f3b3-4956-842a-8b6c0d6e2b36" />

The Client class exemplfifes this one task ideology, it runs getID which has simple logic to make a unique client id for every client. Next, addCar is run, where a car is linked to a client by adding it to a dictionary. This encourages reuse and mainatains code simpilicty.



- use of stubs
<img width="499" height="99" alt="image" src="https://github.com/user-attachments/assets/44b6dedd-4229-4e98-8109-710052015309" />
Originally, my generalised Person class only had drivers license and name, as these were attirbutes I beleive everyone entering the mechanic shop would have. However, I realised I needed a getID method in both Clients and Employees at the shop, so I used a stub in a method getID: 



This allowed me to use a subprogram/method before its logic had actually been coded. This centralized code and set up consistency.
<img width="492" height="165" alt="image" src="https://github.com/user-attachments/assets/c4297650-71bb-4934-81b1-60bb48704a6c" />



- use of control structures and data structures
<img width="656" height="129" alt="image" src="https://github.com/user-attachments/assets/274c18b5-03a0-471c-9009-e62f572438f2" />

This while statement starts an infinte loop that ensures a valid license number is inputted, it requires a number string to pass the check and exit the loop with break, otherwise you will be asked to retry with a valid input.



- ease of maintenance:
  Code is organised into clearly defined classes and subprograms, inheritance is simple and clear, and code is easy to understand. Data and attributes are privatised and encapsulated so they cant be directly accessed outside of their intended class. All of this increases ease of maintenance and modularity.



- version control:
Evolution of code can be seen through gtihub commits, I can track changes, read commit messages and revert to previously working code if needed. Relevant text files are stored in github so I can see what external data is used.



- regular backup:
  By storing code and pushing to github, I have a safe backup of code even if I was to lose my files or vscode project,
