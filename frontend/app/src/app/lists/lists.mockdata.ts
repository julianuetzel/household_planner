import { List } from "./lists";

export const LISTS: List[] = [
    {
        id: '1', title: 'Einkaufsliste', items: [
            {id: 'a', text: 'Äpfel', status: 0, list_id: '1'},
            {id: 'b', text: 'Birnen', status: 0, list_id: '1'},
            {id: 'c', text: 'Klopapier', status: 0, list_id: '1'},
            {id: 'd', text: 'Saft', status: 0, list_id: '1'},
            {id: 'e', text: 'Milch', status: 0, list_id: '1'},
            {id: 'f', text: 'Tee', status: 0, list_id: '1'},
        ]
    },
    {
        id: '2', title: 'To Do Julia täglich', items: [
            {id: 'f', text: 'Abtrockenen', status: 1, list_id: '2'},
            {id: 'g', text: 'Saugen', status: 1, list_id: '2'},
            {id: 'h', text: 'Abspühlen', status: 0, list_id: '2'},
            {id: 'i', text: 'Gassi', status: 1, list_id: '2'},
            {id: 'j', text: 'Bett machen', status: 0, list_id: '2'},
        ]
    },
    {
        id: '3', title: 'To Do Markus täglich', items: [
            {id: 'k', text: 'Abtrockenen', status: 0, list_id: '3'},
            {id: 'l', text: 'Kochen', status: 0, list_id: '3'},
            {id: 'm', text: 'Abspühlen', status: 0, list_id: '3'},
            {id: 'n', text: 'Müll rausbringen', status: 0, list_id: '3'},
            {id: 'o', text: 'Nachtrunde Gassi', status: 0, list_id: '3'},
        ]
    },
    {
        id: '4', title: 'To Do wöchentlich', items: [
            {id: 'p', text: 'Wäsche waschen', status: 0, list_id: '4'},
            {id: 'q', text: 'Abstauben', status: 0, list_id: '4'},
            {id: 'r', text: 'Einkaufen', status: 0, list_id: '4'},
        ]
    },
    {
        id: '5', title: 'Filme', items: [
            {id: 't', text: 'Matrix', status: 0, list_id: '5'},
            {id: 'u', text: 'Zurück in die Zukunft', status: 0, list_id: '5'},
            {id: 'v', text: 'The Green Mile', status: 0, list_id: '5'},
            {id: 'w', text: 'Oppenheimer', status: 0, list_id: '5'},
        ]
    }
  ]
  