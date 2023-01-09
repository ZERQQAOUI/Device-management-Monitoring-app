import mysql.connector
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle,Spacer
from reportlab.lib import colors
from reportlab.rl_config import defaultPageSize
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, inch

PAGE_HEIGHT=defaultPageSize[1]
PAGE_WIDTH=defaultPageSize[0]
styles=getSampleStyleSheet()
Title = "rapport racapulatif"
def myFirstPage(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold',16)
    canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
    canvas.setFont('Times-Roman',9)
    canvas.drawString(inch, 0.75 * inch,"First Page / %s" % pageinfo)
    canvas.restoreState()

def go():
    pdf=SimpleDocTemplate("rapport de routeur .pdf")
    flow_obj=[]
    flow_obj1=[]
    td=[["idtableroutage","rx_destination","masque","passerelle","interface","metrique"]]
    td2=[["Nom","Type","@Mac","num_port","Vlan","debit","etat"]]
    conn=mysql.connector.connect(host='localhost',
      user='root',
      password='root2002',
      database='mld')
    cur=conn.cursor()
    cur.execute("select * from tableroutage")
    rows=cur.fetchall()
    for row in rows:
        td.append(row)
    table=Table(td)
    ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.black)])
    table.setStyle(ts)
    flow_obj.append(table)
    pdf.build(flow_obj)


def went():
    pdf=SimpleDocTemplate("rapport de switch.pdf")
    flow_obj1=[]
    td2=[["Nom","Type","@Mac","num_port","Vlan","debit","etat"]]
    conn=mysql.connector.connect(host='localhost',
      user='root',
      password='root2002',
      database='mld')
    cur=conn.cursor()
    cur.execute("select nom, switch.type, adressemac, num, nomvlan,debit, etat from port, switch ,vlan , portvlan where port.idswitch=switch.idswitch and portvlan.idvlan=vlan.idvlan and port.idport=portvlan.idport")
    rows=cur.fetchall()
    for row in rows:
        td2.append(row)
    table=Table(td2)
    ts=TableStyle([("GRID",(0,0),(-1,-1),2,colors.black)])
    table.setStyle(ts)
    flow_obj1.append(table)
    pdf.build(flow_obj1)

    
if __name__ == "__main__":
    go()
    went()
  
