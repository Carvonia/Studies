#include <stdio.h>

#define TOTAL_CANDIDATOS = 1000

typedef struct {
    float notas[5];
    float media;
    int aprovado;
} Candidato;

void entrada_dados(Candidato candidatos[], int total_candidatos) {
    for (int i = 0; i < total_candidatos; i++) {
        printf("\nCandidato %d:\n", i + 1);
        for (int j = 0; j < 4; j++) {
            do {
                printf("Informe a nota da disciplina %d: ", j + 1);
                scanf("%f", &candidatos[i].notas[j]);
            } while (candidatos[i].notas[j] < 0 || candidatos[i].notas[j] > 10);
        }
    }
}

void calcular_medias(Candidato candidatos[], int total_candidatos) {
    for (int i = 0; i < total_candidatos; i++) {
        float soma_notas = 0;
        float soma_pesos = 0;
        for (int j = 0; j < 4; j++) {
            soma_notas += candidatos[i].notas[j] * (j == 0 ? 4 : (j == 1 ? 3 : (j == 2 ? 2 : 1)));
            soma_pesos += (j == 0 ? 4 : (j == 1 ? 3 : (j == 2 ? 2 : 1)));
        }
        candidatos[i].media = soma_notas / soma_pesos;
        candidatos[i].aprovado = (candidatos[i].media >= 7) ? 1 : 0;
    }
}

void listar_candidatos(Candidato candidatos[], int total_candidatos) {
    printf("\nListagem de candidatos:\n");
    for (int i = 0; i < total_candidatos; i++) {
        printf("\nCandidato %d:\n", i + 1);
        printf("Notas: ");
        for (int j = 0; j < 4; j++) {
            printf("%.2f ", candidatos[i].notas[j]);
        }
        printf("\nMédia: %.2f\n", candidatos[i].media);
        printf("Situação: %s\n", (candidatos[i].aprovado) ? "Aprovado" : "Reprovado");
    }
}

int main() {
    int total_candidatos;
    Candidato candidatos[MAX_CANDIDATOS];

    printf("Informe o número total de candidatos (até 1000): ");
    scanf("%d", &total_candidatos);

    entrada_dados(candidatos, total_candidatos);
    calcular_medias(candidatos, total_candidatos);
    listar_candidatos(candidatos, total_candidatos);

    return 0;
}
