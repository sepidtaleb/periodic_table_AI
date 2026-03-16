import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QHBoxLayout, QLineEdit, QVBoxLayout, QSizePolicy , QTextEdit
from dotenv import load_dotenv
import openai
import os
# Load the .env file
load_dotenv()

# Access the variables
api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL")

openai.api_key = api_key


model_name = 'mistralai/Mistral-Small-3.2-24B-Instruct-2506'

# color scheme similar to many periodic tables
CATEGORY_COLORS = {
    "alkali metal": "#d9534f",
    "alkaline earth metal": "#f0ad4e",
    "transition metal": "#5bc0de",
    "post-transition metal": "#9370db",
    "metalloid": "#f7e463",
    "nonmetal": "#90ee90",
    "halogen": "#66cdaa",
    "noble gas": "#ffb6c1",
    "lanthanide": "#6fa8dc",
    "actinide": "#76d7c4",
    "unknown": "#d3d3d3"
}

# atomic_number, symbol, name, row, column, category
elements = [
(1,"H","Hydrogen",0,0,"nonmetal"),
(2,"He","Helium",0,17,"noble gas"),

(3,"Li","Lithium",1,0,"alkali metal"),
(4,"Be","Beryllium",1,1,"alkaline earth metal"),
(5,"B","Boron",1,12,"metalloid"),
(6,"C","Carbon",1,13,"nonmetal"),
(7,"N","Nitrogen",1,14,"nonmetal"),
(8,"O","Oxygen",1,15,"nonmetal"),
(9,"F","Fluorine",1,16,"halogen"),
(10,"Ne","Neon",1,17,"noble gas"),

(11,"Na","Sodium",2,0,"alkali metal"),
(12,"Mg","Magnesium",2,1,"alkaline earth metal"),
(13,"Al","Aluminium",2,12,"post-transition metal"),
(14,"Si","Silicon",2,13,"metalloid"),
(15,"P","Phosphorus",2,14,"nonmetal"),
(16,"S","Sulfur",2,15,"nonmetal"),
(17,"Cl","Chlorine",2,16,"halogen"),
(18,"Ar","Argon",2,17,"noble gas"),

(19,"K","Potassium",3,0,"alkali metal"),
(20,"Ca","Calcium",3,1,"alkaline earth metal"),
(21,"Sc","Scandium",3,2,"transition metal"),
(22,"Ti","Titanium",3,3,"transition metal"),
(23,"V","Vanadium",3,4,"transition metal"),
(24,"Cr","Chromium",3,5,"transition metal"),
(25,"Mn","Manganese",3,6,"transition metal"),
(26,"Fe","Iron",3,7,"transition metal"),
(27,"Co","Cobalt",3,8,"transition metal"),
(28,"Ni","Nickel",3,9,"transition metal"),
(29,"Cu","Copper",3,10,"transition metal"),
(30,"Zn","Zinc",3,11,"transition metal"),
(31,"Ga","Gallium",3,12,"post-transition metal"),
(32,"Ge","Germanium",3,13,"metalloid"),
(33,"As","Arsenic",3,14,"metalloid"),
(34,"Se","Selenium",3,15,"nonmetal"),
(35,"Br","Bromine",3,16,"halogen"),
(36,"Kr","Krypton",3,17,"noble gas"),

(37,"Rb","Rubidium",4,0,"alkali metal"),
(38,"Sr","Strontium",4,1,"alkaline earth metal"),
(39,"Y","Yttrium",4,2,"transition metal"),
(40,"Zr","Zirconium",4,3,"transition metal"),
(41,"Nb","Niobium",4,4,"transition metal"),
(42,"Mo","Molybdenum",4,5,"transition metal"),
(43,"Tc","Technetium",4,6,"transition metal"),
(44,"Ru","Ruthenium",4,7,"transition metal"),
(45,"Rh","Rhodium",4,8,"transition metal"),
(46,"Pd","Palladium",4,9,"transition metal"),
(47,"Ag","Silver",4,10,"transition metal"),
(48,"Cd","Cadmium",4,11,"transition metal"),
(49,"In","Indium",4,12,"post-transition metal"),
(50,"Sn","Tin",4,13,"post-transition metal"),
(51,"Sb","Antimony",4,14,"metalloid"),
(52,"Te","Tellurium",4,15,"metalloid"),
(53,"I","Iodine",4,16,"halogen"),
(54,"Xe","Xenon",4,17,"noble gas"),

(55,"Cs","Caesium",5,0,"alkali metal"),
(56,"Ba","Barium",5,1,"alkaline earth metal"),
(57,"La","Lanthanum",5,2,"lanthanide"),
(72,"Hf","Hafnium",5,3,"transition metal"),
(73,"Ta","Tantalum",5,4,"transition metal"),
(74,"W","Tungsten",5,5,"transition metal"),
(75,"Re","Rhenium",5,6,"transition metal"),
(76,"Os","Osmium",5,7,"transition metal"),
(77,"Ir","Iridium",5,8,"transition metal"),
(78,"Pt","Platinum",5,9,"transition metal"),
(79,"Au","Gold",5,10,"transition metal"),
(80,"Hg","Mercury",5,11,"transition metal"),
(81,"Tl","Thallium",5,12,"post-transition metal"),
(82,"Pb","Lead",5,13,"post-transition metal"),
(83,"Bi","Bismuth",5,14,"post-transition metal"),
(84,"Po","Polonium",5,15,"post-transition metal"),
(85,"At","Astatine",5,16,"halogen"),
(86,"Rn","Radon",5,17,"noble gas"),

(87,"Fr","Francium",6,0,"alkali metal"),
(88,"Ra","Radium",6,1,"alkaline earth metal"),
(89,"Ac","Actinium",6,2,"actinide"),
(104,"Rf","Rutherfordium",6,3,"transition metal"),
(105,"Db","Dubnium",6,4,"transition metal"),
(106,"Sg","Seaborgium",6,5,"transition metal"),
(107,"Bh","Bohrium",6,6,"transition metal"),
(108,"Hs","Hassium",6,7,"transition metal"),
(109,"Mt","Meitnerium",6,8,"transition metal"),
(110,"Ds","Darmstadtium",6,9,"transition metal"),
(111,"Rg","Roentgenium",6,10,"transition metal"),
(112,"Cn","Copernicium",6,11,"transition metal"),
(113,"Nh","Nihonium",6,12,"unknown"),
(114,"Fl","Flerovium",6,13,"unknown"),
(115,"Mc","Moscovium",6,14,"unknown"),
(116,"Lv","Livermorium",6,15,"unknown"),
(117,"Ts","Tennessine",6,16,"halogen"),
(118,"Og","Oganesson",6,17,"noble gas"),
]

lanthanides = [
(58,"Ce","Cerium"),(59,"Pr","Praseodymium"),(60,"Nd","Neodymium"),
(61,"Pm","Promethium"),(62,"Sm","Samarium"),(63,"Eu","Europium"),
(64,"Gd","Gadolinium"),(65,"Tb","Terbium"),(66,"Dy","Dysprosium"),
(67,"Ho","Holmium"),(68,"Er","Erbium"),(69,"Tm","Thulium"),
(70,"Yb","Ytterbium"),(71,"Lu","Lutetium")
]

actinides = [
(90,"Th","Thorium"),(91,"Pa","Protactinium"),(92,"U","Uranium"),
(93,"Np","Neptunium"),(94,"Pu","Plutonium"),(95,"Am","Americium"),
(96,"Cm","Curium"),(97,"Bk","Berkelium"),(98,"Cf","Californium"),
(99,"Es","Einsteinium"),(100,"Fm","Fermium"),(101,"Md","Mendelevium"),
(102,"No","Nobelium"),(103,"Lr","Lawrencium")
]


class PeriodicTable(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Periodic Table")
        self.resize(1400,700)
        self.setMaximumSize(1600,1200)

        main_layout = QVBoxLayout()
        table_layout = QGridLayout()
        table_layout.setSpacing(3)
        #table_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        #for r in range(10):
        #    table_layout.setRowMinimumHeight(r, 65)

        #to avoid stretch
        for i in range(18):
            table_layout.setColumnStretch(i, 0)

        for i in range(25):
            table_layout.setRowStretch(i, 0)

        self.question_label = QLabel("Ask your question:")
        self.question_label.setStyleSheet(f"font-size: 14px;font-weight: bold;")
        self.question_label.hide()

        # Create an input field for the question
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type your question here...")
        self.input_field.setFixedWidth(1000)
        self.input_field.hide()  # Hide by default

        # Create a submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.hide()
        self.submit_button.setFixedWidth(120)
        self.submit_button.clicked.connect(self.process_question)

        # Create a reset button
        self.reset_button = QPushButton("reset")
        self.reset_button.hide()
        self.reset_button.setFixedWidth(120)
        self.reset_button.clicked.connect(self.reset_question)

        # Create a label to display the answer
        self.answer_label = QTextEdit()
        self.answer_label.setStyleSheet("font-size: 14px;")
        self.answer_label.setFixedWidth(1000)  # Set a fixed width for the answer label
        self.answer_label.setFixedHeight(120)
        self.answer_label.hide()  # Hide by default

        # Layout for input field and submit button
        self.input_layout = QHBoxLayout()
        self.input_layout.addWidget(self.input_field)
        self.input_layout.addWidget(self.submit_button)
        self.input_layout.addWidget(self.reset_button)


        # Add the question label, input field, and answer label to a vertical table_layout
        self.question_layout = QVBoxLayout()
        self.question_layout.addWidget(self.question_label)
        self.question_layout.addWidget(self.input_field)
        self.question_layout.addWidget(self.answer_label)



        self.selected_symbol = ""
        self.selected_name = ""

        for num,symbol,name,row,col,cat in elements:

            text=f"{num}\n{symbol}\n{name}"

            btn=QPushButton(text)
            btn.setFixedSize(60, 60)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            color=CATEGORY_COLORS.get(cat,"#cccccc")

            btn.setStyleSheet(f"""
            QPushButton {{
            background-color:{color};
            border-radius: 6px;
            }}
            QPushButton:hover {{
                    background-color: #555;
                }}
            """)
            btn.clicked.connect(lambda _, s=symbol, n=name: self.show_question_prompt(s, n))
            table_layout.addWidget(btn,row,col)

        # lanthanides
        start_col=3
        for i,(num,symbol,name) in enumerate(lanthanides):

            text=f"{num}\n{symbol}\n{name}"

            btn=QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color:#6fa8dc;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
            """)
            btn.setFixedSize(60, 60)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            btn.clicked.connect(lambda _, s=symbol, n=name: self.show_question_prompt(s, n))
            table_layout.addWidget(btn,8,start_col+i)

        # actinides
        for i,(num,symbol,name) in enumerate(actinides):

            text=f"{num}\n{symbol}\n{name}"

            btn=QPushButton(text)
            btn.setStyleSheet("""
                QPushButton {
                    background-color:#76d7c4;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #555;
                }
            """)
            btn.setFixedSize(60, 60)
            btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

            btn.clicked.connect(lambda _, s=symbol, n=name: self.show_question_prompt(s, n))
            table_layout.addWidget(btn,9,start_col+i)

        title = QLabel("Periodic Table")
        title.setStyleSheet("""
                font-size: 24px;
                font-weight: bold;
                font-family: 'Times New Roman'; """)
        table_layout.addWidget(title, 1, 5, 1,3)

        '''
        input_layout = QGridLayout()
        input_field = QLineEdit()
        input_field.setPlaceholderText("Enter something...")
        input_layout.addWidget(input_field, 0, 0)
        table_layout.addLayout(input_layout, 20, 7, 1, 5)
'''
        main_layout.addLayout(table_layout)
        main_layout.addStretch()
        main_layout.addLayout(self.question_layout)
        main_layout.addLayout(self.input_layout)
        self.setLayout(main_layout)

    def show_question_prompt(self, symbol, name):
        self.selected_symbol = symbol
        self.selected_name = name
        print(f"Button clicked: {symbol}, {name}")  # Debugging line
        """Show the question prompt and input field for the selected element."""
        self.question_label.setText(f"Ask your question about {name} ({symbol}):")
        self.question_label.show()
        self.input_field.show()
        self.submit_button.show()
        self.answer_label.show()
        self.input_field.clear()
        #self.answer_label.clear()
        # Adjust the window size to accommodate the question and answer box
        self.resize(1400, 800)

    def process_question(self):
        """Retrieve the question and update the answer label."""
        question = self.input_field.text()
        # Here you can add logic to process the question and generate an answer
        symbol = self.selected_symbol
        name = self.selected_name
        #self.answer_label.setText(f"Your question about {symbol}: {question}")
        self.open_ai(name, symbol, question)
        self.reset_button.show()


    def open_ai(self, name , symbol, question):
        client = openai.OpenAI(
            api_key=api_key,
            base_url=base_url
        )

        response = client.chat.completions.create(
            model=model_name,  # model to send to the proxy
            messages=[
                {
                    "role": "user",
                    "content": f"Answer the following question about the element {name} ({symbol}) with maximum 500 character: {question}"
                },
            ]
        )
        assistant_response = response.choices[0].message.content
        self.answer_label.setPlainText(assistant_response)
        print(assistant_response)

    def reset_question(self):
        """Clear the input and answer fields for a new question."""
        self.input_field.clear()
        self.answer_label.clear()




app=QApplication(sys.argv)

window=PeriodicTable()
window.setStyleSheet("""
    window {
        background-color: black;
        color: white;
    }
    """)
window.show()

sys.exit(app.exec())
