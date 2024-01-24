<template>
  <div class="applications">
    <h3>Applications list</h3>

    <v-icon>mdi-delete</v-icon>

    <v-data-table :headers="headers" :items="applications" item-key="id">
      <template v-slot:body="{ items }">
        <tbody>
          <tr v-for="(item, index) in items" :key="index">
            <td>{{ item.first_name }}</td>
            <td>{{ item.last_name }}</td>
            <td>{{ item.gender }}</td>
            <td>{{ item.phone_number }}</td>
            <td>
              <v-icon>mdi-delete</v-icon>
            </td>
          </tr>
        </tbody>
      </template>
    </v-data-table>
  </div>
</template>

<script>

export default {
  data(){
    return{
      applications: [],
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Gender', value: 'gender' },
        { text: 'Phone number', value: 'phone_number' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      errors : {}
    }
  },
  methods: {
    getAllApplications(){
      fetch('http://localhost:8000/api/applications/',{
        method: 'GET'
      })
      .then(response => response.json())
      .then((data)=>{
        console.log(data)
        this.applications = data;
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  mounted(){
      this.getAllApplications()
  }
}
</script>

<style scoped>

</style>