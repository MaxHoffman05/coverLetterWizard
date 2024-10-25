# Cover Letter Wizard

> Python program to semi-automate the creation of cover letters.

## Getting Started

To clone this repository enter this command below to clone it to your local folder:

                git clone https://github.com/MaxHoffman05/coverLetterWizard

After navigating to the repository folder you can run the command below after installing python:

                python3 coverLetterWizard.py


## Automating the Process Further
To make the process easier you can hardcode your information into the variables below:
<i>

- name
- phoneNumber
- email
  </i>

You will also want to replace the <i>variables</i> <i>paragraph1</i>, <i>paragraph2</i>, <i>paragraph3</i>, ... with your own written paragraphs. You can also add more paragraphs just make sure they are added to the respective <i>secondPara</i> and <i>thirdPara</i> array variables and in the correct tuple format: ('name of paragraph', paragraphString).

You will also want to change the intro and closing paragraphs to your own intro and closing paragraphs. In your intro paragraph if you include the phrases below they will be replaced with the entered information:

-`<Job Title>` - This will be the title of the job you are applying for </br> 
-`<Company>` - Company you are applying for </br> 
-`<Job Website>` - Website you found the position on </br>

In your closing paragraph if you choose to make a standard closing paragraph you can include the below phrases and they will be replaced:

-`<Company>` - Company you are applying for </br> 
-`<skill1>`, `<skill2>`, `<skill3>` - Skills or details you mentioned in previous paragraphs that you want to mention </br>


The program will output the cover letter to a .txt file formatted as well as in the console formatted. Below is a sample output:

    John Doe
    (555)-555-5555
    johndoe@youremail.com
    October 25, 2024

    Dear Hiring Manager,
        This is an example intro. You can make this whatever you want! I would recommend including keywords like the Bob the Builder website, Bob The Builder & Co., and Carpenter so these can be replaced later!
        In my previous role at [Previous Company], I successfully managed [describe a relevant task or responsibility] and consistently met or exceeded performance goals. I am particularly skilled in [specific skill or tool], which has enabled me to [mention a positive outcome, like improve efficiency, reduce costs, etc.]. My experiences have prepared me well to make a meaningful impact on your team from day one.
        I am especially drawn to this role at [Company Name] because of your commitment to [mention something unique about the company, such as innovation, sustainability, customer experience, etc.]. I believe that my proactive approach and attention to detail would complement your culture and support the team's goals. I am enthusiastic about the opportunity to contribute fresh ideas and be part of a company that values [relevant attribute].
        This is an example outro. You can make this whatever you want! However, I would recommend including the skills you covered in the rest of the cover letter here. You can do this by including woodworking, plumbing, and my heavy machinery license. The skills you entered will automatically be placed in each skill spot. You might also want to reference the Bob The Builder & Co. as well.

    Thank you, 
    John Doe


I would recommend transferring the contents generated in the .txt file to rich text file like a Word Document. The text will stay formatted!
