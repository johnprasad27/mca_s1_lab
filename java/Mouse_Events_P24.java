import java.awt.event.*;
import javax.swing.*;

public class Mouse_Events_P24 extends JFrame {

    public Mouse_Events_P24() {
        setTitle("Mouse Events Demo");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        addMouseListener(new MouseAdapter() {
            public void mouseClicked(MouseEvent e) {
                System.out.println("Clicked at (" + e.getX() + ", " + e.getY() + ")");
            }

            public void mousePressed(MouseEvent e) {
                System.out.println("Pressed at (" + e.getX() + ", " + e.getY() + ")");
            }

            public void mouseReleased(MouseEvent e) {
                System.out.println("Released at (" + e.getX() + ", " + e.getY() + ")");
            }

            public void mouseEntered(MouseEvent e) {
                System.out.println("Entered at (" + e.getX() + ", " + e.getY() + ")");
            }

            public void mouseExited(MouseEvent e) {
                System.out.println("Exited at (" + e.getX() + ", " + e.getY() + ")");
            }
        });

        addMouseMotionListener(new MouseMotionAdapter() {
            public void mouseDragged(MouseEvent e) {
                System.out.println("Dragged to (" + e.getX() + ", " + e.getY() + ")");
            }

            public void mouseMoved(MouseEvent e) {
                System.out.println("Moved to (" + e.getX() + ", " + e.getY() + ")");
            }
        });

        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.out.println("Window closed");
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new Mouse_Events_P24().setVisible(true);
        });
    }
}