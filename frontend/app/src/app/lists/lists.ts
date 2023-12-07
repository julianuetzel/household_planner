export interface List {
    title: string;
    id: string;
    items: Item[];
}

export interface Item {
    id: string;
    text: string;
    status: number;
    list_id: string;
}
