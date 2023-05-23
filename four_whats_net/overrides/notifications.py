
import frappe
from frappe import _
from frappe.email.doctype.notification.notification import Notification, get_context, json
import requests

class ERPGulfNotification(Notification):
    
    def validate(self):
        self.validate_four_whats_settings()
        super(ERPGulfNotification, self).validate()
    
    def validate_four_whats_settings(self):
        settings = frappe.get_doc("Four Whats Net Configuration")
        if self.enabled and self.channel == "4Whats.net":
            if not settings.token or not settings.api_url or not settings.instance_id:
                frappe.throw(_("Please configure 4Whats.net settings to send WhatsApp messages"))
            
    def send(self, doc):
        context = get_context(doc)
        context = {"doc": doc, "alert": self, "comments": None}
        if doc.get("_comments"):
            context["comments"] = json.loads(doc.get("_comments"))

        if self.is_standard:
            self.load_standard_properties(context)
            
        try:
            if self.channel == '4Whats.net':
                self.send_whatsapp_msg(doc, context)
        except:
            frappe.log_error(title='Failed to send notification', message=frappe.get_traceback())
        super(ERPGulfNotification, self).send(doc)
        
    
    def send_whatsapp_msg(self, doc, context):
        settings = frappe.get_doc("Four Whats Net Configuration")
        recipients = self.get_receiver_list(doc, context)
        receiverNumbers = []
        for receipt in recipients:
            number = receipt
            if "{" in number:
                number = frappe.render_template(receipt, context)
            message=frappe.render_template(self.message, context)        
            phoneNumber = self.get_receiver_phone_number(number)
            receiverNumbers.append(phoneNumber)
            url = f"{settings.api_url}/sendMessage/?instanceid={settings.instance_id}&token={settings.token}&phone={phoneNumber}&body={message}"
            response = requests.get(url)
        frappe.msgprint(_(f"Whatsapp message sent to {','.join(receiverNumbers)}"))
    
    def get_receiver_phone_number(self, number):
        phoneNumber = number.replace("+","").replace("-","")
        if phoneNumber.startswith("+") == True:
            phoneNumber = phoneNumber[1:]
        elif phoneNumber.startswith("00") == True:
            phoneNumber = phoneNumber[2:]
        elif phoneNumber.startswith("0") == True:
            if len(phoneNumber) == 10:
                phoneNumber = "966" + phoneNumber[1:]
        else:
            if len(phoneNumber) < 10: 
                phoneNumber ="966" + phoneNumber
        if phoneNumber.startswith("0") == True:
            phoneNumber = phoneNumber[1:]
        
        return phoneNumber   