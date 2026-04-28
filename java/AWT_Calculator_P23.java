import java.awt.*;
import java.awt.event.*;

public class AWT_Calculator_P23 extends Frame implements ActionListener {
    TextField t = new TextField();
    Button b1 = new Button("+");
    Button b2 = new Button("=");

    int num1, num2;

    AWT_Calculator_P23() {
        setLayout(new FlowLayout());
        add(t);
        add(b1);
        add(b2);

        b1.addActionListener(this);
        b2.addActionListener(this);

        setSize(300, 200);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == b1) {
            num1 = Integer.parseInt(t.getText());
            t.setText("");
        } else if (e.getSource() == b2) {
            num2 = Integer.parseInt(t.getText());
            t.setText(String.valueOf(num1 + num2));
        }
    }

    public static void main(String[] args) {
        new AWT_Calculator_P23();
    }
}