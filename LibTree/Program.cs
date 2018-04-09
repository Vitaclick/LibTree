using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Security.Cryptography;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using Google.Apis.Sheets.v4;
using Google.Apis.Util.Store;
using IronPython.Hosting;
using Microsoft.Scripting.Hosting;

namespace LibTree
{
  class Program {
    private static string clientSecret = "secret.json";
    private static readonly string[] scope = {SheetsService.Scope.Spreadsheets};
    private static readonly string appName = "LibTree";
    private static readonly string sheetId = "1HLsMD4mmRXiKXQ4wMYcHFYD3BmaoGmmHvZbNIv_Ado8";
    static void Main(string[] args) {
      Console.OutputEncoding = Encoding.UTF8;
      var libPath = @"C:\Drive\BIM4US\Ресурсы\Artpot\Семейства";
      var data = listFilesInDirectory(libPath);
      Debug.Write(data);

      
    }

    private static SheetsService getService(UserCredential credential) {
      return new SheetsService(new BaseClientService.Initializer {
        HttpClientInitializer = credential,
        ApplicationName = appName
      });
    }
    private static UserCredential getSheetCredential(string clientSecret, string[] scope) {
      using (var stream = new FileStream(clientSecret, FileMode.Open, FileAccess.Read)) {
        var credPath = Path.Combine(Directory.GetCurrentDirectory(), clientSecret);
        return GoogleWebAuthorizationBroker.AuthorizeAsync(
          GoogleClientSecrets.Load(stream).Secrets,
          scope,
          "user",
          CancellationToken.None,
          new FileDataStore(credPath, true)).Result;
      }
    }
    static List<string[]> listFilesInDirectory(string libPath) {
      var opts = SearchOption.AllDirectories;
      var fileFilterPattern = "*.*";
      var filePaths = Directory.GetFiles(libPath, fileFilterPattern, opts);
      var fileData = new List<string[]>();
      foreach (string filePath in filePaths) {
//        var directoryInfo = new DirectoryInfo(libPath);
        var fileInfo = new FileInfo(filePath);
        fileData.Add(new []{ filePath , fileInfo.Name, fileInfo.LastAccessTimeUtc.ToString()});
      }
      return fileData;
    }
  }
}
