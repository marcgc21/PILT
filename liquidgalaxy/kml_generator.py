from races.models import Participant, RaceParticipant,Position,CompetitionTaskParticipantPosition,CompetitionTaskParticipant
import os, errno, random





def create_competitiontaskparticipant_kml(taskparticipant):
    positions = CompetitionTaskParticipantPosition.objects.all().filter(taskparticipant=taskparticipant)
    path="static/kml/" + str(taskparticipant.task.competition.pk) + "/" + taskparticipant.task.name

    r = lambda: random.randint(0, 255)
    color = ('ff%02X%02X%02X' % (r(), r(), r()))

    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    filename="static/kml/" + str(taskparticipant.task.competition.pk) + "/" + taskparticipant.task.name + "/" + str(taskparticipant.pk) + ".kml"

    os.system("touch %s" % (filename))

    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\"colorLine\">\n" +
            "\t\t\t<LineStyle>\n" +
            "\t\t\t\t<color>"+color+"</color>\n" +
            "\t\t\t\t<width>20</width>\n" +
            "\t\t\t</LineStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<styleUrl>#colorLine</styleUrl>\n" +
            "\t\t\t<LineString>\n" +
            "\t\t\t\t<tessellate>1</tessellate>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>\n")
        for position in positions:
            kml_file.write(
                "\t\t\t\t" + str(position.longitude) + "," + str(position.latitude) + "," + str(position.height) + "\n")
        kml_file.write("\t\t\t\t</coordinates>\n" +
                       "\t\t\t</LineString>\n" +
                       "\t\t</Placemark>\n" +
                       "\t</Document>\n" +
                       "</kml>")
        kml_file.close()
        taskparticipant.kmlpath = filename
        taskparticipant.save()

        return filename

def create_routeparticipant_kml(positions,raceparticipant):
    filename = "static/kml/" + raceparticipant.participant.user.username + ".kml"
    auxImagePath = raceparticipant.participant.image.split("&")
    imagePath = auxImagePath[0] + "&amp;" + auxImagePath[1]

    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\"" + raceparticipant.participant.user.username + "\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<scale>2.0</scale>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + imagePath + "</href>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Style id=\"thickBlackLine\">\n" +
            "\t\t\t<LineStyle>\n"+
            "\t\t\t\t<color>ff000000</color>\n" +
            "\t\t\t\t<width>20</width>\n" +
            "\t\t\t</LineStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<styleUrl>#thickBlackLine</styleUrl>\n" +
            "\t\t\t<LineString>\n" +
            "\t\t\t\t<tessellate>1</tessellate>\n" +
            "\t\t\t\t<coordinates>\n")
        for position in positions:
            kml_file.write("\t\t\t\t" + str(position.longitude) +","+ str(position.latitude)+","+str(position.height)+ "\n")
        kml_file.write("\t\t\t\t</coordinates>\n" +
            "\t\t\t</LineString>\n" +
           "\t\t</Placemark>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<name>" + raceparticipant.participant.user.username + "</name>\n" +
            "\t\t\t<description>The participant"+ raceparticipant.participant.user.username +"</description>\n" +
            "\t\t\t<styleUrl>#"+raceparticipant.participant.user.username+"</styleUrl>\n" +
            "\t\t\t<Point>\n" +
            "\t\t\t\t<extrude>1</extrude>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>" +
            str(position.longitude) + "," + str(position.latitude) + "," +str(position.height) +
            "</coordinates>\n" +
            "\t\t\t</Point>\n" +
            "\t\t</Placemark>\n" +
            "\t</Document>\n" +
            "</kml>")
        kml_file.close()
        return filename





def create_participant_kml(positions,raceparticipant):
    filename="liquidgalaxy/kml/"+raceparticipant.participant.user.username+".kml"
    positions=list(positions)
    position=positions[-1]
    auxImagePath= raceparticipant.participant.image.split("&")
    imagePath=auxImagePath[0]+"&amp;"+auxImagePath[1]
    with open(filename, "w") as kml_file:
        kml_file.write(
            "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" +
            "<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n" +
            "\t<Document>\n" +
            "\t\t<Style id=\""+raceparticipant.participant.user.username+"\">\n" +
            "\t\t\t<IconStyle>\n" +
            "\t\t\t\t<scale>2.0</scale>\n" +
            "\t\t\t\t<Icon>\n" +
            "\t\t\t\t\t<href>" + imagePath + "</href>\n" +
            "\t\t\t\t</Icon>\n" +
            "\t\t\t</IconStyle>\n" +
            "\t\t</Style>\n" +
            "\t\t<Placemark>\n" +
            "\t\t\t<name>" + raceparticipant.participant.user.username + "</name>\n" +
            "\t\t\t<description>The participant"+ raceparticipant.participant.user.username +"</description>\n" +
            "\t\t\t<styleUrl>#"+raceparticipant.participant.user.username+"</styleUrl>\n" +
            "\t\t\t<Point>\n" +
            "\t\t\t\t<extrude>1</extrude>\n" +
            "\t\t\t\t<altitudeMode>relativeToGround</altitudeMode>\n" +
            "\t\t\t\t<coordinates>" +
            str(position.longitude) + "," + str(position.latitude) + "," +
            str(position.height) +
            "</coordinates>\n" +
            "\t\t\t</Point>\n" +
            "\t\t</Placemark>\n" +
            "\t</Document>\n" +
            "</kml>")
        kml_file.close()

def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""