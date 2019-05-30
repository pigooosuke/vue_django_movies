//
// models
//

export interface KeyValue {
  key: string;
  value: string | null;
}

// export interface Movie {
//   id: string;
//   title: string;
//   genres: KeyValue[];
//   ratings: KeyValue[];
// }

export interface Movie {
  id: string;
  name: string;
  genres :KeyValue[];
}
