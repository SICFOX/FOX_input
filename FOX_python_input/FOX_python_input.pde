import processing.net.*;

int port = 10001; // 適当なポート番号を設定
int state = 0;

Server server;

void setup() {
  size(400, 400);
  server = new Server(this, port);
  println("server address: " + server.ip()); // IPアドレスを出力
}

void draw() {
  Client client = server.available();

  if (client !=null) {
    String whatClientSaid = client.readString();
    if (whatClientSaid != null) {
      //println(whatClientSaid); // Pythonからのメッセージを出力
      switch (int(whatClientSaid)){
        case 0:
          background(0);
          break;
        case 1:
          background(255);
          server.write("[01]Processingから送っているよ！");
          break;
        case 2:
          background(255, 0, 0);
          server.write("[02]Processingから送っているよ！");
          break;
        case 3:
          background(0, 255, 0);
          server.write("[03]Processingから送っているよ！");
          break;
        case 4:
          background(0, 0, 255);
          server.write("[04]Processingから送っているよ！");
          server.write("Processingから送っているよ！4");
          break;
      }
    }
  }
}
