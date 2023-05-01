import java.util.Collections;
import java.util.Objects;
import java.util.Set;
import java.util.TreeSet;

/**
 * Un étudiant. Les étudiants peuvent suivre des cours, et on un nom et un ID unique.
 * <p>
 * Il n'est <bold>pas</bold> valide de créer deux étudiants avec le même ID.
 */
public class Student {

  /**
   * Le nom de l'étudiant.
   */
  public final String name;

  /**
   * L'ID unique de l'étudiant.
   */
  public final int id;

  /**
   * Les noms des cours que cet étudiant suit. En lecture seule.
   */
  public final Set<String> courses;

  /**
   * Équivalent de `courses` mais avec droit d'écriture.
   */
  private final Set<String> followed;

  public Student(String name, int id) {
    this.name = name;
    this.id = id;
    this.followed = new TreeSet<>();
    this.courses = Collections.unmodifiableSet(followed);
  }

  /**
   * Fait suivre le cours donné à cet étudiant.
   */
  public void take(String course) {
    followed.add(course);
  }

  /**
   * Enlève le cours donné de cet étudiant.
   */
  public void drop(String course) {
    followed.remove(course);
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    Student student = (Student) o;
    return id == student.id &&
        Objects.equals(name, student.name) &&
        Objects.equals(courses, student.courses);
  }

  /**
   * {@inheritDoc}
   */
  @Override
  public int hashCode() {
    return Objects.hash(name, id, courses);
  }
}
