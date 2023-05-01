import java.util.HashMap;
import java.util.Random;

public class App {

  public static void main(String[] args) {
    simulate();
  }

  private static void simulate() {
    var random = new Random();

    var classes = new String[]{"SwEng", "SDP", "DB", "OS", "Algo", "ML"};
    var rooms = new String[]{"BC 05", "BC 06", "BC 07", "BC 08", "BC 09", "BC 10"};
    var students = Database.students().limit(100).toArray(Student[]::new);

    // Au début de la journée, chaque étudiant choisit une salle aléatoire pour étudier.
    var locations = new HashMap<Student, String>();
    for (var student : students) {
      var location = rooms[random.nextInt(rooms.length)];
      locations.put(student, location);
    }

    // Pendant la journée, chaque étudiant peut (ou pas) se préparer à un examen aléatoire.
    for (var student : students) {
      if (random.nextBoolean()) {
        var course = classes[random.nextInt(classes.length)];
        student.take(course);
        System.out.println(student.name + " is preparing for " + course + ".");
      } else {
        System.out.println(student.name + " is taking a day off.");
      }
    }

    // À la fin de la journée, chaque étudiant quitte sa salle.
    for (var student : students) {
      locations.remove(student);
    }

    System.out.println("See you tomorrow !");

    // Les bâtiments devraient être vides. Le sont-ils ?
    if (!locations.isEmpty()) {
      throw new AssertionError("Some classrooms are not empty!");
    }
  }
}
