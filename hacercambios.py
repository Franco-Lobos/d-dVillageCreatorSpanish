i = 0

people = {
    1: ['juan'],
    2: ['asd'], 
    3: ['paco']
}

tam = max(people.keys())

while i < tam:
    guardar people[i]
    i = i+1



   def savechanges(self, name):
        data = self.createdataframe(name)
        modo = self.metodoescritura(f"{self.name}.xlsx")
        writer = pd.ExcelWriter(f"{directorio}/Aldea_{self.name}.xlsx", mode = f"{modo}", engine = "openpyxl")
        data.to_excel(writer, f"People", index=False)
        writer.save()
        writer.close()


    def createdataframe(self, name):
        if self.status == 'new':
            df = pd.DataFrame()
            df['numberid'] = None
            df['name'] = None
            df['lastname'] = None
            df['age'] = None
            df['strength'] = None
            df['job'] = None
            df['lider'] = None
            df['status'] = None
            counterid = 0
        else:
            df = pd.read_excel(f'{directorio}/Aldea_{name}.xlsx', sheet_name= 'People')
            counterid = int(df.iloc[-1, 0])
        for i in self.people:
            inumb = i + counterid
            df.loc[inumb] = [inumb, self.people[i][0], self.people[i][1], self.people[i][2], self.people[i][3], self.people[i][4], self.people[i][5], self.people[i][6]]
            print(i*100/len(self.people), '%')
        return df


            for i in self.people:
            inumb = i + counterid
            df.loc[inumb] = [inumb, self.people[i][1], self.people[i][2], self.people[i][3], self.people[i][4], self.people[i][5], self.people[i][6], self.people[i][7]]
            Gestor.loadingbar(i, len(self.people)})


            loc[counterid] = pd.DataFrame(list(self.people.values()), columns= columnas)