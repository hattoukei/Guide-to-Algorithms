package DataStructures.Java;

import java.util.Stack;

public class Main {
  public static void main(String[] args) {
    Stack<String> stack = new Stack<String>();

    // Pushes items to the stack.
    stack.push("One");
    stack.push("Two");
    stack.push("Three");
    stack.push("Four");

    // For loop to add items to the stack.
    for (int i = 0; i < 10; i++) {
      stack.push("Two");
    }

    // Searches for the index of an element in the stack.
    // From top of the stack to the bottom, indices of elements are as follows:
    // [1, 2, 3, 4, 5.., n]
    // If the element is not found, returns -1.
    System.out.println(stack.search("Two"));

    // Prints out the first item of the stack. Uses stack.peek() which returns
    // the first element.
    System.out.println(stack.peek());

    // Pops items from the stack. Returns the removed item.
    String element = stack.pop();

    // Returns true or false depending on if stack is empty.
    System.out.println(stack.empty());

    // Prints the stack.
    System.out.println(stack);
    System.out.println(element);

    // Stacks are useful for:
    // 1. undo/redo features
    // 2. moving back/forward through browser history
    // 3. backtracking algorithms (maze, file directories)
    // 4. calling functions (call stack)
  }
}
