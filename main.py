from pyscript import display, document

classlist = []

class StudentAddition():
    def __init__(self, name, section, favsub):
        self.name = name
        self.section = section
        self.favsub = favsub

    def introduce(self):
        return f"{self.name} from {self.section} loves the {self.favsub} subject."


def show_creds(e):
    favsub = document.getElementById('input1').value
    name = document.getElementById('input2').value
    section = document.getElementById('input3').value

    student1 = StudentAddition(name, section, favsub)
    classlist.append(student1)

    display(f'{student1.name} from {student1.section} loves the {student1.favsub} subject.', target='output')

listStudent = [
    StudentAddition('Ivy Zosa', '10-Topaz', 'TLE'),
    StudentAddition('Calvin Garcia', '10-Topaz', 'Math'),
    StudentAddition('Harmony Yao', '10-Topaz', 'Music'),
    StudentAddition('Khloe Espina', '10-Topaz', 'Math'),
    StudentAddition('Carl Rufo', '10-Topaz', 'Social Studies')
]

def show_class(e):
    list = document.getElementById('output').innerHTML = ''

    for i in listStudent:
        display(i.introduce(), target='output')

    for i in classlist:
        display(i.introduce(), target='output')





