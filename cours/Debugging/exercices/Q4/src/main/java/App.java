import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.stream.IntStream;

public class App {

  public static void main(String[] args) {
    sorting();
  }

  private static void sorting() {
    // Prendre 100 nombres
    var numbers = IntStream.range(0, 100).boxed().toArray(Integer[]::new);
    Collections.shuffle(Arrays.asList(numbers));

    // Les trier d'après leur ordre naturel
    Quicksort.sort(numbers, Comparator.naturalOrder());

    // Imprimer le résultat
    System.out.println(Arrays.toString(numbers));
  }
}
