'''
Cover Letter Wizard
Author: Max Hoffman
Date: 10/24/2024 - 10/25/2024
Purpose: Make the process of creating cover letters easier! 
Creates a .txt file already formated with your pre-made paragraphs and information

'''
import datetime



#Enter custom paragraph instead of the ones in the arrays
def customParagraph():
    inputP = input('Enter your custom paragraph: \n')
    return inputP

#display each tuple in the arrays for paragraphs 
def displayParagraphs(arr):
    count = 0
    print('------------------')
    for i in arr:
        print(str(count) + ' -> ' + i[0])
        count += 1
    print('------------------\n\n')

#to make sure the user enters a correct length phone number since it is formatted for the cover letter
def enterNumber():
    num = ''
    while(len(num) != 10):
        num = input('Enter your phone number: \n')
        
    return num

#method to choose a paragraph from the 2nd and 3rd paragraph arrays, try except to make sure a valid number is entered in the array
def chooseParagraph(arr, finishedCoverLetter):
    while True:
        try:
            displayParagraphs(arr)
            inputLetter = int(input('Custom (-1) paragraph or one of the paragraphs above (enter number) ? '))

            finishedCoverLetter += '\t'
            if(inputLetter == -1):
                customP = customParagraph()
                finishedCoverLetter += customP
                newFile.write("\t" + customP)
                break;
            elif 0 <= inputLetter and inputLetter < len(arr):
                finishedCoverLetter += arr[int(inputLetter)][1]
                newFile.write("\t" + arr[int(inputLetter)][1])
                break;
            else:
                print('Enter a valid number between 0 and '+ str(len(arr)-1))
        except ValueError:
            print('Invalid character - Enter a number')
        except IndexError:
            print('Enter a number between 0 and ' + str(len(arr)-1))
    finishedCoverLetter += '\n\n'
    newFile.write("\n")

#! Enter basic info

name = input('Enter Your Name: \n')
phoneNumber = str(input('Enter your phone number: \n'))
if(len(phoneNumber) != 10):
    phoneNumber = enterNumber()
phoneNumber = f"({phoneNumber[:3]})-{str(phoneNumber)[3:6]}-{str(phoneNumber)[6:]}"
email = input('Enter your email: \n')

'''
IF you would like to hardcode these variables comment the above code and uncomment the below code
name = 'your name'
phoneNumber = 5555555555
email= 'your email'

'''
#Job specific details
companyName = input('Enter Company Name: \n')
title = input('Enter Job Title: \n')
website = input('Enter website job was found on: \n')
currdate = datetime.datetime.now()
date = currdate.strftime("%B %d, %Y")

#creating signature and header from info
signature = 'Thank you, \n' + name
finishedCoverLetter = name + '\n' + phoneNumber + '\n' + email + '\n' + date + '\n\n Dear Hiring Manager,\n'

#create file with your name and the job title in the name of the file
newFile = open(name + ' ' + title + ' Cover Letter.txt', "a")
newFile.write(finishedCoverLetter)



#! Arrays for all paragraphs that we will use to build the text file, holds tuples format: ('Name of paragraph', paragraph string)
secondPara = []
thirdPara = []


#! Each token below will be replaced with the information provided for the job
#<Job Website>  website I found the job posted
#<Company> Company you are applying for
#<Job Title> Title of the job
# first paragraph
#! Each paragraph are example paragraphs and should be replaced with your own information or own paragraphs, you can add more second paragraph and third paragraphs as well
standardIntro = 'This is an example intro. You can make this whatever you want! I would recommend including keywords like <Job Website>, <Company>, and <Job Title> so these can be replaced later!'

#second paragraphs
paragraph1 = 'With a background in [your field/industry] and a passion for continuous learning, I am excited about the opportunity to bring my skills and experience to [Company Name]. Having worked in roles where [mention a relevant skill or responsibility], I have developed a strong foundation that aligns with the requirements of this position. I am eager to contribute to your team and help drive [mention a key goal or value of the company].'
secondPara.append(('CS Project', paragraph1))
paragraph2 = 'In my previous role at [Previous Company], I successfully managed [describe a relevant task or responsibility] and consistently met or exceeded performance goals. I am particularly skilled in [specific skill or tool], which has enabled me to [mention a positive outcome, like improve efficiency, reduce costs, etc.]. My experiences have prepared me well to make a meaningful impact on your team from day one.'
secondPara.append(('Previous Role', paragraph2))

#3rd paragraphs
paragraph3 = 'I am especially drawn to this role at [Company Name] because of your commitment to [mention something unique about the company, such as innovation, sustainability, customer experience, etc.]. I believe that my proactive approach and attention to detail would complement your culture and support the team\'s goals. I am enthusiastic about the opportunity to contribute fresh ideas and be part of a company that values [relevant attribute].'
thirdPara.append(('Why I was drawn to the role', paragraph3))
paragraph4 = 'Throughout my career, I have demonstrated a strong commitment to collaboration and problem-solving. At [Previous Company], I worked closely with cross-functional teams to develop solutions for [describe relevant challenge or project]. This experience taught me the importance of adaptability and clear communication, qualities I believe would make me an asset to [Company]. I am confident that my ability to navigate complex situations and work effectively with diverse teams would allow me to make a positive impact on your organization'
thirdPara.append(('My Career', paragraph4))

#closing paragraph
standardClosing = 'This is an example outro. You can make this whatever you want! However, I would recommend including the skills you covered in the rest of the cover letter here. You can do this by including <skill1>, <skill2>, and <skill3>. The skills you entered will automatically be placed in each skill spot. You might also want to reference the <Company> as well.'


#! Replace entered info from basic info section for intro and closing paragraphs
standardIntro = standardIntro.replace('<Job Title>', title)
standardIntro = standardIntro.replace('<Job Website>', website)
standardIntro = standardIntro.replace('<Company>', companyName)
standardClosing = standardClosing.replace('<Company>', companyName)


#? custom or one of the intro paragraphs?
while True:
    try:
        inputLetter = input('Custom (c) or Standard Intro (s) ? ')
        inputLetter = inputLetter.lower()
        finishedCoverLetter += '\t'
        if(inputLetter == 'c') :
            customP = customParagraph()
            finishedCoverLetter += customP
            newFile.write("\t" + customP)
            break;
        elif(inputLetter == 's') : 
            finishedCoverLetter += standardIntro
            newFile.write("\t" + standardIntro)
            break;
        else:
            print('Enter c for custom or, s for Standard Intro paragraph')
    except ValueError:
        print('Invalid character - Enter a letter')
finishedCoverLetter += '\n\n'
newFile.write("\n")


#? custom or one of the secondary paragraphs?
chooseParagraph(secondPara, finishedCoverLetter)

#? custom or third paragraphs ? 
chooseParagraph(thirdPara, finishedCoverLetter)


#? closing paragraph
finishedCoverLetter += '\t'
inputLetter = str(input('Custom (c) closing paragraph or standard (s)?'))
if(inputLetter == 'c'):
    customP = customParagraph()
    finishedCoverLetter += customP
    newFile.write("\t" + customP)
else:
    #Enter in the three things the cover letter focused on
    input1 = input("Enter topic 1:\n")
    input2 = input("Enter topic 2:\n")
    input3  = input("Enter topic 3:\n")
    
    print('You entered the skills : ' + input1 + ' ' + input2 + ' ' + input3)
    #replace skills
    standardClosing = standardClosing.replace('<skill1>', input1)
    standardClosing = standardClosing.replace('<skill2>', input2)
    standardClosing = standardClosing.replace('<skill3>', input3)

    newFile.write("\t" + standardClosing + "\n\n" + signature)
    finishedCoverLetter += standardClosing
#add signature
finishedCoverLetter += '\n\n'
finishedCoverLetter += signature

#display finished product
print('Finished Cover Letter')
print(finishedCoverLetter)
    
newFile.close()

