def lis(arr):
      res = []
      for x,y in arr:
          if not res or y > res[-1]:
              res.append(y)
          else:
              i = bisect_left(res, y)
              res[i] = y

      return len(res)
