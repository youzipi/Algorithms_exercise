package ex;

import java.io.BufferedWriter;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

/**
 * Created by youzipi on 18/1/11 下午4:15
 */
public class BigDataSearch {
    public static final int MAX_COUNT = 1000000;

    public static String genIP() {
        return new StringBuilder()
                .append(Math.random() * 255)
                .append(".")
                .append(Math.random() * 255)
                .append(".")
                .append(Math.random() * 255)
                .append(".")
                .append(Math.random() * 255)
                .append("\n")
                .toString()
                ;
    }

    public static void genFile() {
        Path path = Paths.get("ip.txt");
        try (BufferedWriter writer = Files.newBufferedWriter(path)) {
            for (int i = 0; i < MAX_COUNT; i++) {
                writer.write(genIP());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        BigDataSearch.genFile();
    }
}
