from django.db import models
from django.db.models import Avg, Sum, Count
from django.contrib.auth.models import User


# Create your models here.



class Batch(models.Model):
	farm = models.CharField(max_length=30)
	picture = models.ImageField(upload_to = 'batch/', blank=True, null=True)
	purchased = models.IntegerField()
	unit_price = models.IntegerField()
	projected_SP = models.IntegerField()
	start_date = models.DateField(auto_now_add=False)
	end_date = models.DateField(auto_now_add=False)
	user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return str(self.id)

	def get_all():
		result = Batch.objects.all()
		return result


	@classmethod
	def get_by_id(cls, id):
		result = cls.objects.get(id=id)
		return result
	
	def total_cost(id):
			u_p = list(Batch.objects.filter(id=id).aggregate(Sum('unit_price')).values())
			u_p = int("".join(map(str,u_p)))
			
			purch = list(Batch.objects.filter(id=id).aggregate(Sum('purchased')).values())
			purch = int("".join(map(str,purch)))
			cost = u_p * purch
			return cost

class Customers(models.Model):
	Name = models.CharField(max_length=30)
	number = models.IntegerField()
	date = models.DateField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.DO_NOTHING)


	def __str__(self):
		return str(self.id)

	@classmethod
	def customers_by_batch(cls, id):
		result = Customers.objects.filter(batch = id)
		return result

		
class Deaths(models.Model):
	number = models.IntegerField()
	reason = models.TextField(max_length=300)
	date = models.DateField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)

	@classmethod
	def death_by_batch(cls, id):
		result = Deaths.objects.filter(batch = id)
		return result

	@classmethod
	def death_sum(cls, id):
			table = list(Deaths.objects.filter(batch_id=id).aggregate(Sum('number')).values())
			test = all( i == None for i in table)
			if (test) == True:
					return 1
			else:
					table = int("".join(map(str,table)))
					return table


class ExpenseDetails(models.Model):
	group = models.CharField( max_length=30)
	
	def __str__(self):
			return self.group

class ExpenseGroup(models.Model):
		group = models.CharField( max_length=30, null=True, blank=True)
		details = models.ForeignKey(ExpenseDetails, on_delete=models.DO_NOTHING, null=True, blank=True)
		batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True, blank=True)

	
		def __str__(self):
			return self.group



class Expenses(models.Model):
	amount = models.IntegerField()
	group = models.ForeignKey(ExpenseGroup, on_delete=models.DO_NOTHING, null=True, blank=True)
	details = models.TextField(max_length=300, null=True, blank=True)
	date = models.DateField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)


	def __str__(self):
		return str(f"expense- {self.id}")


	@classmethod
	def exp_by_batch(cls, id):
		result = Expenses.objects.filter(batch = id)
		return result

	@classmethod
	def search(cls, id, group):
			test =  Expenses.objects.filter(batch__id= id, group__group__contains=group)
			return test


	@classmethod
	def sum_by_group_list(cls, id):
		group = ExpenseGroup.objects.all()
		group_list = []
		for i in group:
				group_list.append(i.group)
		yield group_list

	@classmethod
	def sum_by__group_amount(cls, id):
		group = ExpenseGroup.objects.all()
		group_list = []
		for i in group:
				group_list.append(i.group)
		lists = group_list
		for i in lists:

			table =  list(Expenses.objects.filter(batch__id= id, group__group__contains=i).aggregate(Sum('amount')).values())
			test = all( i == None for i in table)
			if (test) == True:
					return 1
			else:
					table = int("".join(map(str,table)))
			yield table


	@classmethod
	def expense_sum(cls, id):
			table = list(Expenses.objects.filter(batch_id=id).aggregate(Sum('amount')).values())
			test = all( i == None for i in table)
			if (test) == True:
					return 1
			else:
					table = int("".join(map(str,table)))
					return table

	@classmethod
	def expense_sum_per(cls, id):
			table = list(Expenses.objects.filter(batch_id=id).values('group').annotate(sum=Sum('amount')))

			# table = table[0]
			# table = table.get('sum')
			table = len(table)

			return table




class Revenue(models.Model):
	sell_price = models.IntegerField()
	number = models.IntegerField()
	date = models.DateField(auto_now_add=False)
	batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
	customer = models.ManyToManyField(Customers)

	def __str__(self):
		return str(self.id)

	@classmethod
	def total_revenue(cls, id):
			s_price = list(Revenue.objects.filter(batch_id=id).aggregate(Sum('sell_price')).values())
			test = all( i == None for i in s_price)
			if (test) == True:
					return 1
			else:
					s_price = int("".join(map(str,s_price)))
			num = list(Revenue.objects.filter(batch_id=id).aggregate(Sum('number')).values())
			test = all( i == None for i in num)
			if (test) == True:
					return 1
			else:
					num = int("".join(map(str,num)))

			total = s_price * num

			return total					
	
