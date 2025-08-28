class Bar {
    void  prt_name(){
        System.out.println("Bar");
    }
}

class Foo{
    void prt_name(){
          System.out.println("Bar");
    }
}


public class main {
    public static void prt(Foo obj){
        obj.prt_name();
    }
    public static void main(String[] args) {
        Bar bar = new Bar();
        Foo foo = new Foo();
        bar.prt_name();
        foo.prt_name();
    }
}