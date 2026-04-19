import kr.dogfoot.hwplib.object.HWPFile;
import kr.dogfoot.hwplib.reader.HWPReader;
import kr.dogfoot.hwpxlib.object.HWPXFile;
import kr.dogfoot.hwpxlib.writer.HWPXWriter;
import kr.dogfoot.hwp2hwpx.Hwp2Hwpx;

public class Convert {
    public static void main(String[] args) throws Exception {
        if (args.length < 2) {
            System.err.println("Usage: java -jar hwp2hwpx-fat.jar input.hwp output.hwpx");
            System.exit(1);
        }
        String input = args[0];
        String output = args[1];

        System.out.println("Reading: " + input);
        HWPFile hwpFile = HWPReader.fromFile(input);

        System.out.println("Converting HWP -> HWPX...");
        HWPXFile hwpxFile = Hwp2Hwpx.toHWPX(hwpFile);

        System.out.println("Writing: " + output);
        HWPXWriter.toFilepath(hwpxFile, output);

        System.out.println("Done!");
    }
}
