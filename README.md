# COMP24011 2024 Lab2

This is the repo for COMP24011 labs in the academic session 2024-25.

This branch holds the materials for the `lab2` assignment.
You can always return to this branch with the command
```
git checkout lab2
```

There is a Unix shell refresh script to fetch the lab materials when they become available.
You **need to** run this script before you start working on the assignment.
This can be done with the command
```
./refresh.sh
```

To submit your work you **must** follow the COMP24011 submission guidelines in the [Laboratory Exercises](https://online.manchester.ac.uk/webapps/blackboard/content/listContentEditable.jsp?content_id=_15828703_1&course_id=_81433_1) Blackboard page.
The lab manual details which files make up the solution of this exercise which you **have to** commit, tag for submission as `lab2_sol`, and then push both the commit and tag to your repo.
This usually involves the following sequence of commands
```
git add -A .
git commit
git tag lab2_sol
git push origin
git push --tags origin
```

There are instructions on coursework submission via GitLab in Appendix L of the [CS UG Handbook](https://online.manchester.ac.uk/bbcswebdav/pid-16350838-dt-content-rid-185496744_1/xid-185496744_1).
These include examples of how to amend your submission and fix the submission tag if you make a mistake before the deadline.
You **must not** try to make changes to the submission tag after your deadline has closed as this may constitute academic malpractice.

Please ask for support in the lab sessions if you're unsure about any lab instructions or submission.

[modeline]: # ( vim:set spell spl=en: )
