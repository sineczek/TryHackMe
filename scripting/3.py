#!/usr/bin/env python
import bufio
import crypto
import crypto
import crypto
import encoding
import fmt
import net
import time

var reader bufio.Reader

func read() []byte {
        p := make([]byte, 2048)
        n, _ := reader.Read(p)
        return p[:n]
}

func main() {
        conn, _ := net.Dial("udp", "10.10.255.14:4000")
        defer conn.Close()
        reader = bufio.NewReader(conn)

        fmt.Fprintf(conn, "hello")

        fmt.Println(string(read()))

        fmt.Fprintf(conn, "ready")

        p := read()
        key := p[4:28]
        fmt.Printf("key (len %d): %s\n", len(key), string(key))

        iv := p[32:44]
        fmt.Printf("iv (len %d): %s\n", len(iv), string(iv))

        checksum := hex.EncodeToString(p[104:136])
        fmt.Println("checksum: " + checksum)

        for {
                fmt.Fprintf(conn, "final")
                flag := read()
                fmt.Printf("decoding flag of size %d: %x\n", len(flag), flag)

                fmt.Fprintf(conn, "final")
                tag := read()
                fmt.Printf("with tag of size %d: %x\n", len(tag), tag)

                ciphertext := append(flag, tag...)
                fmt.Printf("final cipher of size %d: %x\n", len(ciphertext), ciphertext)

                block, _ := aes.NewCipher(key)
                aesgcm, _ := cipher.NewGCM(block)

                plaintext, err := aesgcm.Open(nil, iv, ciphertext, nil)
                if err != nil {
                        fmt.Println("failed to decode with err: " + err.Error())
                        time.Sleep(time.Second)
                        continue
                }

                sha := sha256.Sum256(plaintext)
                hash := hex.EncodeToString(sha[:])
                if hash == checksum {
                        fmt.Println(string(plaintext))
                        break
                }
                fmt.Println("didn't match checksum")
        }
}
