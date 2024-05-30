import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients = []
nicknames = []

print("Server has started...")


questions=[
    "what is italian word for  PIE ? /n a.mozreralla /n b.pasty /n c.patty /n d.pizza",
    "water boils at 212 un its in which scale? /n a.celsius /n b.farenheit /n c.reumer /n d.kelvin",
    "which of the following character is related to lamb /n a.humpy-dumpty /n b.mary /n c.johny /n d.teedy-bear",
    "how many bones does a infant child have? /n a.206 /n b.256 /n c.around 300 /n d.more than 350",
    "Which marvel charactrer has made marvel studios more famous? /n a.captain America /n b.Thor /n c.Iron man /n d.black panther",
    "which of the following element in the periodic table belong sto inert gases /n a.Na /n b.F /n c.Mg /n d.Xe",
    "which is the most haunted fort in india? /n a.gwalior fort /n b.bhangarh fort /n c.golkond afort /n d.kuldhara",
    "who is the first indian mathematician to found vedic maths? /n a.Aryabatta /n b.ramanujan /n c.shakuntala devi /n d. bharathi krishna tirthaji ",
    " To whose memory did shahjahan built TajMahal /n a.babar /n b.akbar /n c.aurangajeb /n d.MumtajBejum",
    "what is the name of the galaxy that we live in? /n a.cygnus /n b.Milky way /n c.Andromeda /n d.Virgo",
    "In which state does the sun rise first in India? /n a.arunachal pradesh/n b.gujarat /n c.sikkim /n d. tamilnadu"

]
answers=['d','b','b','c','a','d','b','d','d','b','a']



def clientthread(conn):
    score=0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("you will a question, the answer to that question would be one of a,b,c,d\n ".encode('utf-8'))
    conn.send("Good luck!!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score +=1
                    conn.send(f"Bravo! Your score is{score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index,question,answer = get_random_question_answer(conn)
            else:
                remove(conn)

        except:
            continue


def get_random_question_answer(conn):
    random_index=random.randint(0,len(questions) - 1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index,random_answer,random_question

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

        
        
while True:
    conn, addr = server.accept()
    conn.send('NICKNAME'.encode('utf-8'))
    nickname = conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.append(nickname)
    message = "{} joined!".format(nickname)
    print(message)
    new_thread = Thread(target= clientthread,args=(conn, nickname))
    new_thread.start()

