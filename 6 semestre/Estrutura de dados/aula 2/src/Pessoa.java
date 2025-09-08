public class Pessoa {
    private String nome;
    private String email;

    @Override
    public String toString() {
        return "nome= " + nome + ", email= " + email;
    }

    public Pessoa (String nome, String email){
        this.nome = nome;
        this.email = email;
    }

    public Pessoa(){
    }

    public String getNome(){
        return this.nome;
    }

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void logar(){
        System.out.println(this.nome + " logado.");
    }
}
