       IDENTIFICATION DIVISION.
       PROGRAM-ID. FILE2PG.
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT INFILE ASSIGN TO "data.txt"
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD INFILE.
       01 IN-RECORD.
           05 F-ID     PIC X(5).
           05 F-NAME   PIC X(20).
           05 F-EMAIL  PIC X(30).

       WORKING-STORAGE SECTION.
       01 WS-END           PIC X VALUE "N".
       01 CMD              PIC X(256).

       PROCEDURE DIVISION.
       MAIN.
           OPEN INPUT INFILE
           PERFORM UNTIL WS-END = "Y"
               READ INFILE
                   AT END
                       MOVE "Y" TO WS-END
                   NOT AT END
                       STRING "psql -h <IP> -U myuser -d mydb -c ""INSERT INTO testdata (id, name, email) VALUES ('"
                           F-ID "', '" F-NAME "', '" F-EMAIL "')""" INTO CMD
                       END-STRING
                       CALL "SYSTEM" USING CMD
               END-READ
           END-PERFORM
           CLOSE INFILE
           STOP RUN.
