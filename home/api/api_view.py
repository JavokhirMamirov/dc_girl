from rest_framework.decorators import api_view
from rest_framework.response import Response

from home.models import User, Question, Answer


@api_view(['GET'])
def get_question(request, pk):
    try:
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            user = User.objects.create(id=pk)
        if user.step == 0:
            data = {
                "success": True,
                "data": {
                    "query": "Ism va Familyangizni kiriting!",
                    "step": 0,
                },
                "finish": False
            }
            user.step = 1
            user.save()
        else:
            try:
                query = Question.objects.get(index=user.step)
                data = {
                    "success": True,
                    "data": {
                        "query": query.query,
                        "step": user.step
                    },
                    "finish": False
                }
            except Question.DoesNotExist:
                data = {
                    "success": True,
                    "data": {},
                    "finish": True
                }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)


@api_view((['POST']))
def set_answer(request, pk):
    try:
        answer = request.data.get("answer")
        if answer is not None:
            try:
                user = User.objects.get(id=pk)
            except User.DoesNotExist:
                user = User.objects.create(id=pk)

            if user.step == 0:
                user.name = answer
                user.step = 1
                user.save()
            else:
                query = Question.objects.get(index=user.step)
                an = Answer.objects.create(
                    query=query,
                    answer=answer
                )
                user.step = user.step + 1
                user.answer.add(an)
                user.save()
            try:
                query = Question.objects.get(index=user.step)
                data = {
                    "success": True,
                    "data": {
                        "query": query.query,
                        "step": user.step
                    },
                    "finish": False
                }
            except Question.DoesNotExist:
                data = {
                    "success": True,
                    "data": {},
                    "finish": True
                }
        else:
            data = {
                "success": True,
                "data": {
                    "query": "Ism va Familyangizni kiriting!",
                    "step": 0

                },
                "finish": False
            }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)


@api_view(['GET', "POST"])
def get_user(request, pk):
    try:
        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            user = User.objects.create(id=pk)
        if request.method == "POST":
            step = request.data.get('step')
            user.step = step
            user.save()
        data = {
            "success": True,
            "data": {
                "step": user.step
            }
        }
    except Exception as err:
        data = {
            "success": False,
            "error": f"{err}"
        }
    return Response(data)
