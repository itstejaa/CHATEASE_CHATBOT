import psycopg2
from rasa.core.channels.channel import InputChannel
from rasa.core.channels.channel import UserMessage
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

class PostgreSQLInput(InputChannel):
    @classmethod
    def name(cls):
        return "postgresql"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_latest_input(self):
        
        conn = psycopg2.connect("dbname=database_name user=username password=password")
        cur = conn.cursor()
        cur.execute("SELECT user_id, message FROM chat_history ORDER BY timestamp DESC LIMIT 1")
        user_id, message = cur.fetchone()
        cur.close()
        conn.close()
        return UserMessage(message, self.sender_id, input_channel=self.name())

    def blueprint(self, on_new_message):
        return []
    def getresults(intent) :

    if intent=="college_departments":
        return """GVPCE Departements are 
                    1.Chemical Engineering
                    2.CSE
                    3.CSE  (Artificial Intelligence and Machine Learning)
                    4.CSE Data Science
                    5.Electrical and Electronics
                    6.Mechanical
                    7.Mechanical (Robotics)
                    8.Civil
                    9.Information Technology
                    10.Electronics and Communication
                    11.Master of computer applications
                    12.M.TECH """
    elif intent=="course offered_offered courses in college":
        return """GVPCE Courses Offered are
                        M.Tech.
                        B.Tech.
                        MCA.
                        B.Tech. (lateral entry)"""
    elif intent=="gvpce college information_information college":
        return """Gayatri Vidya Parishad (GVPCE) College of Engineering (Autonomous) is a private engineering college in Visakhapatnam, Andhra Pradesh, India. The college was established in 1996 by the GVP Society,an educational organization in Visakhapatnam."""
    elif intent=="fee_fee details":
        return """The fee structure at GVPCE 
1)B.Tech: The first year fee is ₹75,900
2)B.Tech (Lateral): The first year fee is ₹75,900
3)M.Tech: The first year fee is ₹55,000
4)MCA: The first year fee is ₹42,200
5)Hostel: The fee is ₹60,000 per year 
"""
        
    elif intent=="student_activities":
        return """GVP College of Engineering conducts the Techno Cultural Festival,which takes place each year in March. 
                  The College mostly supports extracurricular activities such as NSS, dance, and athletics."""
    elif intent=="library_information":
        return """The Library \U0001F4D5 was started in the year 1996, and named as Prof. B. Sarveswara Rao Library in 2005 as a mark of respect to former President Gayatri Vidya Parishad.
                  The Library at GVPCE Visakhapatnam has an extensive collection of books, journals and periodicals, as well as a digital section providing members access to a host of e-resources, including e-books, e-journals and e-magazines.
                  The Digital Library consists of Video Lessons of NPTEL from IIT’s, E-Journals and E-Databases.Remote access facility through Knimbus is available for accessing the e-resources subscribed."""
    elif intent=="about_NAAC":
        return """With an intake of 200 students and four B.Tech. programs in 1996, the college has evolved into an autonomous institution with an intake of 1260 students offering 10 B.Tech. programs,M.Tech. Programs and one MCA program. The curriculum has also evolved over these years offering Choice Based Credit System under Outcome Based Education.
                  These include attaining academic eminence through affiliations and rankings, revolutionizing research endeavors, fostering innovation and entrepreneurship, establishing national/global academic partnerships, and championing sustainability and community development.Accredited twice by NAAC with 'A' Grade with a CGPA of 3.47/4.00"""
    elif intent=="infrastructure_details":
        return """The college campus spans 21 acres, is spread over 33,000 sq. m, and has ample quality standards. The College has a well-equipped library, lab, and hostel accommodation for both male and female students.
                An impressive amount of Gold Medals at the university level have been awarded to students in recent years.Deserving students can apply for financial aid."""
    elif intent=="facilities_information facilities":
        return """The fully Wi-Fi-enabled Campus of GVPCE Visakhapatnam also has a cafeteria, a medical centre, shuttle services, and banking and ATM facilities for the students and staff to avail."""
    elif intent=="collegebus_bus services":
        return """College provides 14 buses that transport students from various parts of the city to the college. The buses also transport the college's professors and associate professors, faculties, and staff.
        The fees of bus facility depends on the distance you travel."""
    elif intent=="hod faculty_professor HOD":
        return """Here are some faculty members at Gayatri Vidya Parishad College of Engineering (Autonomous) (GVPCE):

     1)Dr. M.S.N. Murthy -Head of the Department (Chairman)-Chemical Engineering.

    2)Dr. G. Papa Rao Professor,Department of Civil Engineering -HOD (Chairman).

    3)Dr. K.B. Madhuri -HOD (Chairperson)-CSE.

    4)Dr. N. BalaSubrahmanyam Professor & HOD of ECE.

    5)Prof. N. Siva Prasad Department of Mechanical Engg.

    6)Dr. Y. Anuradha Associate Professor & HOD of MCA.

    for more details visit: https://gvpce.ac.in/bos.html"""
    elif intent=="skill_skill development":
        return """GVPCE  assesses students skill development through design thinking projects, which often involve open-ended problems and subjective evaluation criteria 
                  for more details visit: https://www.gvpce.ac.in/skill.html"""
    elif intent=="placements_info":
        return """GVPCE has a placement rating of 8.3/10. Over 84% of students get placed every year, with the highest package being 42 LPA and the lowest being 3.5 LPA. Some companies that hire students from GVPCE include Amazon, Zoho, factset, capgemini, and TCS.
        (You can contact GVPCE at tnp@gvpce.ac.in, deanplacements@gvpce.ac.in, 0891-2739507.)
         for yearwise placement details visit: https://www.gvpce.ac.in/campusplace.html """
    elif intent=="academic_calendar":
        return "you can go to our website"
    elif intent=="examinations_info":
        return """Gayatri Vidya Parishad College Admission is granted primarily through the Common Entrance Test conducted by the Higher Education Andhra Pradesh State Council and partially through the College management.
                  At the postgraduate level, the College offers the M.Tech and MCA programs. The candidates are chosen based on their performance on the entrance examination, followed by counseling."""
    elif intent=="knowyourcollege_college":
        return """GVPCE offers admission to the B Tech, B Tech (Lateral), M Tech, and MCA. NBA has accredited all the B Tech programs at least twice so far. Gayatri Vidya Parishad College is among four self-funding colleges in AP; MHRD selects under TEQIP to receive an INR 5 Cr for upgrading the quality of PG education, innovation, and research. 
                  The faculty strength is more than 280, out of which 117 are Ph.D. holders. They provide exceptional guidance and training to the students."""
    elif intent=="contact_info":
        return """GVPCE(Autonomous)
            Madhurawada, Visakhapatnam-530048,AP,India
            Telephone No. : 91-891-2739507,Fax:91-891-2739605
            E-Mail :principal@gvpce.ac.in 
            for more details visit: https://gvpce.ac.in/contactus.html"""
    elif intent=="pg_courses":
        return """GVPCe offers PG courses in the following areas:1)MCA
                                                                 2)M.Tech."""
    elif intent=="B-Techadmissions_gvpce btech admission":
        return """B Tech is available in 7 specializations. And M Tech is available in varied engineering disciplines with an annual intake of 18 seats per branch. 
        The College offers admission under two categories: Convenor quota and management quota. 70% of seats will be filled under Convenor Quota. In contrast, 30% of seats are allotted for Management Quota."""
    elif intent=="greet":
        return "Hello there!\U0001F44B I'm ChatEase Yours AI assistant,I'm still learning thanks for your patience\U0001f600..let's get started."
    elif intent=="hgfhjihhgfhgfhgfhwess":
        return """Sorry iam unable to understand\U0001F910"""
    elif intent=="goodbye":
        return """Bye,Have a nice day..\U0001F607"""
    elif intent=="mood_great":
        return """Wonderful..\U0001F642"""
    elif intent=="bot_challenge":
        return """Yes, I am a chatbot! I'm designed to understand and respond to a wide range of inquiries and conversations. Feel free to ask me anything or engage in a conversation on college related topic you like!"""
    elif intent=="eamcetcutoff ranks_btech cutoff to get seat":
        return """Specializations                            Female     Male

                 1.IT                                         7277       6780
                 2.ECE                                        10595      6306
                 3.Chemical                                   27998      21529
                 4.civil                                      12658      84021
                 5.CSE                                        4322       101205
                 6.Mechanical                                 32505      19844  
                 These are the cutoff ranks for both male and female students"""
    elif intent=="timings_college timings":
        return """Gvpce clg open from 8:30 AM to 5 PM.The library is open from 9 AM to 6 PM, except for the second Saturday of the month from 9 AM to 5 PM, and Sundays from 9 AM to 1 PM"""
    elif intent=="hostel_hostelforcollege":
        return """Separate hostels are available for both boys and girls in the campus. Those who desire to join hostel should pay Rs. 60,000/- per annum through DD in favour of “GVP BOYS HOSTEL” (for boys) and “GVP GIRLS HOSTEL (for girls) payable."""
    elif intent=="mechanicalbranch_mechanical engineering":
        return """B.Tech in Mechanical Engineering current intake 120 seats,B.Tech in Mechanical Engineering (Robotics) current intake is 60 seats.
                  fee for mechanical is INR 3.04 Lakh,With almost 90% of students getting placed in the mechanical engineering program"""
    elif intent=="chemicalbranch_chemical engineering":
        return """B.Tech. in Chemical Engineering course at GVPCE is a four-year undergraduate course that admits 60 students.
                  The total tuition fee is INR 3.04 Lakh.With almost 90% of students getting placed in the chemical engineering program """
    elif intent=="CSEbranch_computer science engineering":
        return """B.Tech. in CSE at GVPCE is a 4 years course.The course offers admission to 240 students.
                  The highest package and the lowest package are 42 LPA and 3.5 LPA"""
    elif intent=="ECEbranch_ECE engineering":
        return """B.Tech. in ECE at GVPCE is a 4 years course.The course offers admission to 120 students.More than 70% of students are placed every year. 
                  The highest package and the lowest package are 42 LPA and 3.5 LPA respectively """
    elif intent=="civilbranch_civil engineering":
        return """GVPCE offers a B.Tech. in Civil Engineering program at the UG level.The course is four years long and admits 120 students. The total tuition fee is INR 3.04 Lakh."""
    elif intent=="ITbranch_ IT engineering":
        return """The IT program includes specializations such as: Artificial Intelligence and Machine Learning and Data Sciences
                  The GVPCE college has 240 seats for the IT department """
    elif intent=="MTECHCOURSE_MTECH":
        return """GVPCE offers an M.Tech in Computer Science Engineering. The two-year course and the total tuition fee is INR 1.10 Lakh.
                The program includes,
                1)Pedagogy training,
                2)Dissertation work,
                3)Research facilities,
                4)GATE stipend: INR 12,400 per month from MHRD, Government of India"""
    elif intent=="MCA_masterofcomputerapplications":
        return """MCA at Gvpce is a 2 years course at the PG level. The course offers admission to 60 students.
                The  tuition fee for MCA is INR 1.12 Lakh.Tuition fee is calculated on the basis of 1st year/semester.Actual amount may vary.
                Almost 75–80 percent of the students got placed with an average package of 4 LPA and the highest package of 11 LPA,
                for more details visit: https://gvpce.ac.in/contactus.html"""
    elif intent=="staffmca_mcadepartment":
        return """DETAILS ABOUT MCA department
                  1)Dr.Y.Anuradha(HOD)
                  2)Mrs.V.Lakshmi(Assistant Professor)
                  3)Dr.N jaya Lakshmi(Assosciate Professor)
                  4)Mr.P.V.V.R.Chandra Sekhar(Assistant professor)
                  5)Ms.Bharathi Sadhu(Assistant Professor)
                  6)Mr.B.Bala Krishna(Assistant Professor)
                  7)Mr.K.Saran Kumar(Assistant Professor)"""
    elif intent=="sports_games sports in college":
        return """College avail facilities spread over 6.5 acres for the following games:
1)Basketball,
2)Ball Badminton,
3)Cricket practicing Nets,
4)Table Tennis,
5)Tenni-coit,
6)Tennis.
These facilities are open from 6 A.M. to 8.00 A.M. and 3.30 P.M. to 7 P.M."""
    elif intent=="chairperson_principal of college":
        return """1)Dr. A.B. Koteswara Rao(chairman)
                  2)Prof. Dr. N. Ramesh Babu Institute Chair Professor.
                  3)P.S. Rao(founder of gvpce)"""
    elif intent=="labs in college_laboratory in gvpe college":
        return """GVPCE has labs for CIVIL,IT,CSE,MECH,MCA,and other dept. Here are some of the labs at GVPCE:
1)Computer Based Training Lab,
2)Manufacturing CNC Lab,
3)Electronics Home,
4)Electronics Office,
5)Manufacturing Welding Lab,
6)Web Technologies & Web Services Lab,
7)Data Mining Lab,
8)Control Systems & Simulation Lab,in association with APSSDC and SIEMENS """
    elif intent=="internships in college_workshop in gvpce":
        return """GVPCE offers internships and industry projects in the final year of B.Tech,M.Tech and MCA programs. The college also offers a two-week workshop on programming skills for first-year students."""
    elif intent=="canteen in college_foodcourt in gvpce":
        return """GVPCE has a cafeteria that serves healthy, nutritious, and hygienic meals and snacks to students at reasonable prices. 
        The canteen is modern and hygienic, and offers dine-in seating."""
    elif intent=="gym _health physical gvpce":
        return """The college has indoor facilities with Table Tennis, Caroms, Chess, 12 stations multi gym for and 4 stations gym.
        The gym is open from 6 AM–8 AM and 3:30 PM–7 PM."""
    elif intent=="office timings _college office timings":
        return """The office timings are from 9:00 am to 5:00pm """
    elif intent=="pay of fee _college fee payment process":
        return """The fee is to be paid thro’ Demand Draft / Banker’s Cheque, as the case may be, from any of the nationalized banks drawn in favour of Principal,
          G.V.P.College of Engineering (Autonomous) payable at Visakhapatnam."""
    elif intent=="information":
        return """Hello there,I am the virtual assistant of gvpce powered by AI.
        If you get stuck,you can always restart our conversations.If not try contact to our admin
        TEJA by mail tteja3333@gmail.com  """
    
    else:
        return """oops!\U0001F612,I couldn't find what you were looking for. Post this Query to our email: tteja3333@gmail.com
        Please ensure that the query contains relevant college details so"""

if __name__ == "__main__":
    interpreter = RasaNLUInterpreter("path_to_your_nlu_model")
    agent = Agent.load("path_to_your_dialogue_model", interpreter=interpreter)
    input_channel = PostgreSQLInput()
    agent.handle_channels([input_channel], http_port=5004)
