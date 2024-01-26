<template>
  <v-container>
    <div class="applications">
    <h3>Applications list</h3>
    <v-data-table :headers="headers" :items="applications" item-key="id">
      <template v-slot:body="{ items }">
        <tbody>
          <tr v-for="(item, index) in items" :key="index">
            <td>{{ item.first_name }}</td>
            <td>{{ item.last_name }}</td>
            <td>{{ item.gender }}</td>
            <td>{{ item.phone_number }}</td>
            <td>{{ item.application_status }}</td>
            <td>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="primary" @click="openViewDialog(item)" v-bind="attrs" v-on="on" >mdi-eye</v-icon>
                </template>
                <span>View application details</span>
              </v-tooltip>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="error" class="icon" @click="openRejectDialog(item)" v-bind="attrs" v-on="on" >mdi-window-close</v-icon>
                </template>
                <span>Reject application</span>
              </v-tooltip>
              <v-tooltip top>
                <template v-slot:activator="{ on, attrs }">
                  <v-icon color="success" class="icon" @click="openApproveDialog(item)" v-bind="attrs" v-on="on" >mdi-check-bold</v-icon>
                </template>
                <span>Approve application</span>
              </v-tooltip>
            </td>
          </tr>
        </tbody>
      </template>
    </v-data-table>

    <!-- View application details Dialog -->
    <v-dialog v-model="viewDialog" max-width="600">
      <v-card>
        <v-card-title>Application details</v-card-title>
        <v-card-text>
          <p><strong>First name:</strong>  {{ selectedApplication.first_name }}</p>
          <p><strong>Last name:</strong> {{ selectedApplication.last_name }}</p>
          <p><strong>Date of birth:</strong>  {{ selectedApplication.date_of_birth }}</p>
          <p><strong>Gender:</strong> {{ selectedApplication.gender }}</p>
          <p><strong>Email:</strong>  {{ selectedApplication.email }}</p>
          <p><strong>Phone number: </strong>{{ selectedApplication.phone_number }}</p>
          <p><strong>Address:</strong> {{ selectedApplication.address }}</p>
          <p><strong>Current class:</strong>  {{ selectedApplication.current_class }}</p>
          <p><strong>School:</strong> {{ selectedApplication.school }}</p>
          <p><strong>School location:</strong>  {{ selectedApplication.school_location }}</p>
          <p><strong>School phone number:</strong> {{ selectedApplication.school_phone_number }}</p>
          <p><strong>Reason for change:</strong> {{ selectedApplication.change_reason }}</p>
        </v-card-text>
        <v-card-actions>
          <v-btn @click="closeViewDialog" >Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- Reject application dialog -->
    <v-dialog v-model="rejectDialog" max-width="600" >
      <v-card>
        <v-card-title>Reject application</v-card-title>
        <v-card-text>
          <h4>Are you sure you want to reject this application?</h4>
        </v-card-text>
        <v-card-actions>
          <v-btn variant="elevated" color="error" @click="handleRejectApplication(rejectedApplication.id)">Reject application</v-btn>
          <v-btn variant="elevated" color="secondary" @click="closeRejectDialog">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
  </v-container>
</template>

<script>

export default {
  data(){
    return{
      applications: [],
      errors : {},
      viewDialog: false,
      rejectDialog: false,
      approveDialog: false,
      selectedApplication: {},
      rejectedApplication: {},
      approvedApplication: {},
      headers: [
        { text: 'First Name', value: 'first_name' },
        { text: 'Last Name', value: 'last_name' },
        { text: 'Gender', value: 'gender' },
        { text: 'Phone number', value: 'phone_number' },
        { text: 'Application status', value: 'application_status' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
      
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
    },

    // View application dialog
    openViewDialog(application){
      this.selectedApplication = application;
      this.viewDialog = true;
    },
    closeViewDialog(){
      this.selectedApplication = {};
      this.viewDialog = false;
    },

    // Reject application dialog
    openRejectDialog(application){
      this.rejectedApplication = application;
      this.rejectDialog = true;
    },
    closeRejectDialog(){
      this.rejectedApplication = {};
      this.rejectDialog = false;
    },
    handleRejectApplication(id){
      fetch(`http://localhost:8000/api/applications/reject/${id}/`,{
        method : 'GET' 
      })
      .then((response)=>{
        if(response.ok){
          console.log('Rejected successfully')
        }
        this.closeRejectDialog();
        this.$router.go(0);
      })
      .catch((err)=>{
        console.log(err);
      })
    },

    // Approve application dialog
    openApproveDialog(application){
      this.approvedApplication = application;
      this.approveDialog = true;
    },
    closeApproveDialog(){
      this.approvedApplication = {};
      this.approveDialog = false;
    },
  },
  mounted(){
      this.getAllApplications()
  }
}
</script>

<style scoped>
  .icon{
    margin-left: 15px;
  }
</style>