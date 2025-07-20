let Persons = [
    { Name: "Harry", Age: 14 },
    { Name: "Ethan", Age: 30 },
    { Name: "Peter", Age: 21 },
    { Name: "Clark", Age: 42 },
    { Name: "John",  Age: 34 },
    { Name: "Alice", Age: 16 }
]

let Names = [];

for (let i = 0; i < Persons.length; i++) {
    if (Persons[i].Age >= 18) {
        Names.push(Persons[i].Name);
    }
}

let AdultPerson = Persons.filter((Person) => Person.Age > 18);
console.log(Names);
console.log(AdultPerson);

let UpdatedAge = Persons.map((Person) => Person.Age < 18 ? { ...Person, Age : Person.Age + 1 } : Person);
console.log(UpdatedAge);

let Message = Persons.find((P) => P.Name == 'John') ? Persons.map((Person) => Person.Name == 'John' ? { ...Person, Name: 'Johnweak' } : Person) : "John Is Not Present";
console.log(Message);

// Add New Person In A Given Array

let Name = 'Trump';
let Age = 73;

Persons = [...Persons, { Name, Age }];

console.log(Persons);

// All the Person Age Wise

Persons.sort((a, b) => a.Age - b.Age);
console.log(Persons);

// Remove Persos Less Than Age 18

Persons = Persons.filter((Person) => Person.Age >= 18);
console.log(Persons);

