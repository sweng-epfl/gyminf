import java.util.Comparator;

/**
 * Une classe avec une méthode implémentant l'algorithme Quicksort.
 */
public class Quicksort {

  private Quicksort() {
    // Not instantiable.
  }

  /**
   * Trie le tableau donné avec Quicksort.
   *
   * @param elements le tableau à trier
   * @param <T>      le type des éléments du tableau
   */
  public static <T> void sort(T[] elements, Comparator<T> comparator) {
    sort(elements, comparator, 0, elements.length);
  }

  // Trie les éléments dans l'intervale donné
  private static <T> void sort(T[] elements, Comparator<T> comparator, int from, int until) {
    if (from > until) {
      return;
    }
    var pivot = partition(elements, comparator, from, until);
    sort(elements, comparator, from, pivot);
    sort(elements, comparator, pivot, until);
  }

  // Partitionne les éléments dans l'intervalle donné autour d'un pivot, et retourne son index
  private static <T> int partition(T[] elements, Comparator<T> comparator, int from, int until) {
    var p = elements[from];
    var s = until;
    for (var i = until - 1; i > from; i--) {
      if (comparator.compare(elements[i], p) > 0) {
        s--;
        swap(elements, i, s);
      }
    }
    swap(elements, from, s);
    return s - 1;
  }

  // Inverse la position de deux éléments
  private static <T> void swap(T[] elements, int i, int j) {
    var tmp = elements[i];
    elements[i] = elements[j];
    elements[j] = tmp;
  }
}
