<template>
  <div>
    <v-container>
      <v-form @submit.prevent="handleApplicationSubmission">
        <h3>Apply for vacancy</h3>
        <v-text-field label="First name" v-model="first_name"></v-text-field>
        <v-text-field label="Last name" v-model="last_name" ></v-text-field>
        <v-text-field label="E-mail" v-model="email" ></v-text-field>
        <v-radio-group v-model="gender" label="Gender" >
          <v-radio label="Male" value="male"></v-radio>
          <v-radio label="Female" value="female"></v-radio>
        </v-radio-group>
        <v-text-field label="Date of birth" v-model="date_of_birth" type="date" ></v-text-field>
        <v-text-field label="Phone number" v-model="phone_number"></v-text-field>
        <v-text-field label="Address" v-model="address"></v-text-field>
        <v-select :items="classes" label="Which class are you currently in?" ></v-select>
        <v-text-field label="What is your current school" v-model="school"></v-text-field>
        <v-text-field label="What is your current school location" v-model="school_location"></v-text-field>
        <v-text-field label="What is your current school contact" v-model="school_phone_number"></v-text-field>
        <v-textarea label="What is your reason for changing schools" v-model="change_reason"></v-textarea>
        <v-select :items="classes_to_apply_for" label="Which class are you applying for?"></v-select>
        <v-text-field label="What combination are you interested in doing?" v-model="combination_applied_for"></v-text-field>
        <v-text-field type="file" label="Upload your recommendation letter" v-model="recommendation_letter"></v-text-field>
        <v-text-field type="file" label="Upload your passport sized photo" v-model="passport"></v-text-field>
        <v-text-field type="file" label="Upload a pdf of results from your former school" v-model="results_document"></v-text-field>
        <v-text-field label="Guardian name" v-model="guardian_name"></v-text-field>
        <v-text-field label="Guardian E-mail" v-model="guardian_email"></v-text-field>
        <v-text-field label="Guardian contact/phone number" v-model="guardian_phone_number"></v-text-field>
        <v-text-field label="What is your relationship with the above guardian" v-model="relationship_with_guardian"></v-text-field>
        <v-select label="What is your religion?" :items="religions"></v-select>
        <v-radio-group v-model="disabled" label="Are you disabled in any way?" >
          <v-radio label="No" value="false"></v-radio>
          <v-radio label="Yes" value="true"></v-radio>
        </v-radio-group>
        <v-textarea v-if="disabled === 'true'" label="What is your disability?" v-model="disabled_description"></v-textarea>
        <v-radio-group v-model="any_chronic_disease_condition" label="Do you have any chronic illness?(e.g athma, stroke, HIV, cancer ,etc)" >
          <v-radio label="No" value="false"></v-radio>
          <v-radio label="Yes" value="true"></v-radio>
        </v-radio-group>
        <v-textarea v-if="any_chronic_disease_condition === 'true'" label="What chronic disease do you have?" v-model="chronic_disease_condition_description"></v-textarea>

        <v-btn variant="elevated" color="primary" type="submit" >Submit application</v-btn>

      </v-form>
    </v-container>
  </div>
</template>

<script>
export default {
    data(){
      return{
        first_name: '',
        last_name: '',
        gender: '',
        email: '',
        date_of_birth : null,
        phone_number: '',
        address: '',
        current_class: '',
        school: '',
        school_location: '',
        school_phone_number: '',
        change_reason: '',
        class_applied_for: '',
        recommendation_letter: null,
        passport: null,
        results_document: null,
        guardian_name: '',
        guardian_phone_number: '',
        guardian_email: '',
        relationship_with_guardian: '',
        religion: '',
        combination_applied_for: '',
        disabled: false,
        disabled_description: '',
        any_chronic_disease_condition: false,
        chronic_disease_condition_description: '',

        classes: ['P7 Vac','F1', 'F2', 'F3', 'F4', 'F4 Vac', 'F5', 'F6'],
        classes_to_apply_for: ['F1', 'F2', 'F3', 'F4', 'F5', 'F6'],
        religions: ['Islam','Christianity']

      }
    },
    methods:{
      handleApplicationSubmission (){
        console.log(
          this.first_name,  this.last_name,  this.gender,
          this.email, this.date_of_birth, this.phone_number,
           this.address, this.current_class, this.school
          , this.school_location, this.school_phone_number,
           this.change_reason, this.class_applied_for,
           this.recommendation_letter, this.passport,
           this.results_document, this.guardian_name,
          this.guardian_email, this.guardian_phone_number,
           this.relationship_with_guardian, this.religion,
           this.combination_applied_for, this.disabled,
           this.disabled_description, this.any_chronic_disease_condition,
           this.chronic_disease_condition_description
        )
        const applicationData = { 
          first_name: this.first_name, last_name: this.last_name, gender: this.gender,
          email: this.email,date_of_birth: this.date_of_birth,phone_number: this.phone_number,
          address: this.address,current_class: this.current_class,school: this.school
          ,school_location: this.school_location,school_phone_number: this.school_phone_number,
          change_reason: this.change_reason,class_applied_for: this.class_applied_for,
          recommendation_letter: this.recommendation_letter,passport: this.passport,
          results_document: this.results_document,guardian_name: this.guardian_name,
          guardian_email: this.guardian_email,guardian_phone_number: this.guardian_phone_number,
          relationship_with_guardian: this.relationship_with_guardian,religion: this.religion,
          combination_applied_for: this.combination_applied_for,disabled: this.disabled,
          disabled_description: this.disabled_description,any_chronic_disease_condition: this.any_chronic_disease_condition,
          chronic_disease_condition_description: this.chronic_disease_condition_description
          
        }
        fetch('http://localhost/api/applications/apply',{
          method: 'POST',
          headers:{
            'Content-Type':'application/json'
          },
          body: JSON.stringify(applicationData)
        }).then((response)=>{
            if(response.status === 201){
              console.log("Application submitted successfully")

            this.first_name = '',  this.last_name = '',  this.gender = '',
            this.email = '', this.date_of_birth = null, this.phone_number = '',
            this.address = '', this.current_class = '', this.school = '',
            this.school_location = '', this.school_phone_number = '',
            this.change_reason = '', this.class_applied_for = '',
            this.recommendation_letter = null, this.passport = null,
            this.results_document = null, this.guardian_name = '',
            this.guardian_email = '', this.guardian_phone_number = '',
            this.relationship_with_guardian = '', this.religion = '',
            this.combination_applied_for = '', this.disabled = false,
            this.disabled_description = '', this.any_chronic_disease_condition = false,
            this.chronic_disease_condition_description = ''
            }
        }).catch((err)=>{
            console.log(err)
        })
      }
    }
}
</script>

<style scoped>

</style>