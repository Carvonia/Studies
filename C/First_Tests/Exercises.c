#include <stdio.h>
#include <stdlib.h>

#define PESO_P 0.4
#define PESO_M 0.3
#define PESO_I 0.2
#define PESO_C 0.1

float notas[1000][5];
float media_materia[4];
int aprovado;

void inserir_notas(int candidatos){
    int subchoice;
    int subsubchoice;
    printf("Submenu -Inserir Dados-\n");
    printf("1- Inserir dados do Inicio ao Fim\n 2- Escolher 1 candidato para modificar\n 3- Escolher um candidato para modificar até o fim\n");
    scanf("%d", &subchoice);
    
    switch (subchoice){
        case 1:
            for(int i = 0; i < candidatos; i++){
                printf("Candidato atual: %d\n", i+1);
                for(int j = 0; j < 4; j++){
                    float nota;
                    printf("Informe a nota da disciplina (Portugues, Matematica, Ingles e Computação em ordem): ");
                    scanf("%f", &nota);
        
                    if (nota < 0 || nota > 10) {
                        printf("Nota inválida! Insira uma nota entre 0 e 10.\n");
                        j--;
                    } else {
                        notas[i][j] = nota;
                    }
                }
            }
            system("cls");
            break;
        
        case 2:
            int loop = 1;
            while(loop == 1){
                system("cls");
                printf("Qual candidato deseja modificar? ");
                scanf("%d", &subsubchoice);
                printf("Candidato atual: %d\n", subsubchoice);
                subsubchoice--;
                for(int j = 0; j < 4; j++){
                        float nota;
                        printf("Informe a nota da disciplina (Portugues, Matematica, Ingles e Computação em ordem): ");
                        scanf("%f", &nota);
            
                        if (nota < 0 || nota > 10) {
                            printf("Nota inválida! Insira uma nota entre 0 e 10.\n");
                            j--;
                        } else {
                            notas[subsubchoice][j] = nota;
                        }
                }
                printf("\nDigite (1) caso queira modificar outro participante.\n");
                scanf("%d", &loop);
            }
            system("cls");
            break;
        
        case 3:
            system("cls");
            printf("Qual candidato deseja começar a modificar? ");
            scanf("%d", &subsubchoice);
            for(int i = subsubchoice-1; i < candidatos; i++){
                printf("Candidato atual: %d\n", i+1);
                for(int j = 0; j < 4; j++){
                    float nota;
                    printf("Informe a nota da disciplina (Portugues, Matematica, Ingles e Computação em ordem): ");
                    scanf("%f", &nota);
        
                    if (nota < 0 || nota > 10) {
                        printf("Nota inválida! Insira uma nota entre 0 e 10.\n");
                        j--;
                    } else {
                        notas[i][j] = nota;
                    }
                }
            }
            system("cls");
            break;
        default:
            system("cls");
            break;
    }
    printf("\nAperte -enter- para continuar.");
    system("pause");
    system("cls");
}


void calculo_da_media(int candidatos){
    for(int i=0; i < candidatos; i++){
        float media = 0;
        media += (notas[i][0] * PESO_P) + (notas[i][1] * PESO_M) + (notas[i][2] * PESO_I) +(notas[i][3] * PESO_C);
        notas[i][4] = media;
    }
}

void listagem(int candidatos){
    for(int i=0; i < candidatos; i++){
        printf("Candidato %d\n", i+1);
        printf("Notas:\n");
        printf("Português = %.2f\n", notas[i][0]);
        printf("Matemática = %.2f\n", notas[i][1]);
        printf("Inglês = %.2f\n", notas[i][2]);
        printf("Computação = %.2f\n", notas[i][3]);
        printf("Média: %.2f\n", notas[i][4]);
        if(notas[i][4] >= 7){
            printf("O candidato está classificado!\n");
        } else {printf("O candidato NÃO está classificado!\n");}
        printf("\n");
    }
    printf("\nAperte -enter- para voltar ao menu.");
    system("pause");
}

void materias_media(int candidatos){
    for(int i=0; i < candidatos; i++){
        media_materia[0] += notas[i][0]; 
    }
    media_materia[0] = media_materia[0] / candidatos;

    for(int i=0; i < candidatos; i++){
        media_materia[1] += notas[i][1]; 
    }
    media_materia[1] = media_materia[1] / candidatos;

    for(int i=0; i < candidatos; i++){
        media_materia[2] += notas[i][2]; 
    }
    media_materia[2] = media_materia[2] / candidatos;

    for(int i=0; i < candidatos; i++){
        media_materia[3] += notas[i][3]; 
    }
    media_materia[3] = media_materia[3] / candidatos;

    printf("Media de Português: %.2f\n", media_materia[0]);
    printf("Media de Matemática: %.2f\n", media_materia[1]);
    printf("Media de Inglês: %.2f\n", media_materia[2]);
    printf("Media de Computação: %.2f\n", media_materia[3]);
    printf("\nAperte -enter- para voltar ao menu.");
    system("pause");
}

void main(){
    int candidatos = 1;
    int hemp = 1;

    printf("Insira quantos candidatos você irá avaliar até no máximo 1000: ");
    scanf("%d", &candidatos);
    system("cls");
    if (candidatos > 1000){candidatos = 1000;} else if (candidatos < 1) {candidatos = 1;}

    while (hemp == 1){
        int choice;
        printf("Bem vindo ao sistema de avaliação de candidatos!\n");
        printf("Lista de comandos:\n");
        printf("\n1- Inserir dados");
        printf("\n2- Média de cada disciplina");
        printf("\n3- Listagem de candidatos");
        printf("\n4- Sair do Programa\n");
        scanf("%d", &choice);

        switch (choice){
            case 1:
                inserir_notas(candidatos);  
                calculo_da_media(candidatos);
                system("cls");
                break;

            case 2:
                materias_media(candidatos);
                system("cls");
                break;

            case 3:
                listagem(candidatos);
                system("cls");
                break;

            case 4:
                hemp = 0;
                break;

            default:
                system("cls");
                break;
        }
        
        
    }
}